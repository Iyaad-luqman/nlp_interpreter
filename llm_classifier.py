import json
from langchain_community.llms import Ollama
from schema_validator import is_valid_schema

async def classify_prompt(data):
    options = ["create", "delete", "edit"]
    prompt = "You are are an expert ontologist and have been asked to help a user define an information classifier.The user will input some text. Based on the user input, you are to provide the action which is best suited among the given options, which are" + options+  ". And the user input is "+  data + ".Provide the result response as JSON { \"action\": \"the_action\" } and nothing else."
    try:
        llm = Ollama(model="llama3")
    except Exception as e:
        raise ValueError(f"Failed to initialize LLM model: {e}")

    try:
        initial_prompt = prompt
        response = llm(initial_prompt)
        response_dict = json.loads(response)
        action_value = response_dict.get("action", "")
       
        if action_value in options:
            return response
        else:
            retry_prompt =  prompt +  ". Only use options which i have provided. "
            response_dict = json.loads(retry_prompt)
            action_value = response_dict.get("action", "")
       
            if action_value in options:
                return response
            else:
                raise ValueError("Response does not contain the provided action.")
    except Exception as e:
        return (response)