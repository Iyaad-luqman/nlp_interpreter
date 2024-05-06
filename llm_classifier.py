import json
from langchain_community.llms import Ollama
import llm_switcher

def classify_prompt(data, model_name=None):
    options = ["create", "delete", "edit"]
    prompt = "You are are an expert ontologist and have been asked to help a user define an information classifier.The user will input some text. Based on the user input, you are to provide the action which is best suited among the given options, which are" + str(options)+  ". And the user input is "+  data + ".Provide the result response as JSON { \"action\": \"the_action\" }. ONLY OUTPUT THE JSON and no other text. "
    try:
        nlp_model = llm_switcher.get_nlp_model( model_name=model_name)
    except Exception as e:
        raise ValueError(f"Failed to initialize LLM model: {e}")

    try:
        initial_prompt = prompt
        response = nlp_model.process_text(initial_prompt)
        response_dict = json.loads(response)
        action_value = response_dict.get("action", "")
       
        if action_value in options:
            return response
        else:
            retry_prompt =  prompt +  ". Only use options which i have provided. "
            retry_response = nlp_model.process_text(retry_prompt)
            response_dict = json.loads(retry_response)
            action_value = response_dict.get("action", "")
       
            if action_value in options:
                return response
            else:
                raise ValueError("Response does not contain the provided action.")
    except Exception as e:
        return ("The prompt did not return a valid JSON. Please Debug to know more.")
    

def classify_multiple_prompt(data, model_name=None):
    options = ["create", "delete", "edit"]
    prompt = "You are are an expert ontologist and have been asked to help a user define an information classifier.The user will input some text. Based on the user input, you are to provide the action which is best suited among the given options, which are" + str(options)+  ". Please do note that, It can come under multiple options, so provide all of which it matches. And the user input is "+  data + ".Provide the result response as JSON { \"actions\": [\"the_action1\", \"the_action2\", \"the_action3\"] }. ONLY OUTPUT THE JSON and no other text."
    try:
        nlp_model = llm_switcher.get_nlp_model( model_name=model_name)

    except Exception as e:
        raise ValueError(f"Failed to initialize LLM model: {e}")

    try:
        response = nlp_model.process_text(prompt)
        response_dict = json.loads(response)
        actions = response_dict.get("actions", [])
       
        if not all(action in options for action in actions):
            retry_prompt =  prompt +  ". Only use options which i have provided. "
            retry_response = nlp_model.process_text(retry_prompt)
            response_dict = json.loads(retry_response)
            actions = response_dict.get("actions", [])

       
            if not all(action in options for action in actions):
                raise ValueError("Response does not contain the provided action.")
            else:
                return response
        else:
            return response
    except Exception as e:
        return ("The prompt did not return a valid JSON. Please Debug to know more.")
