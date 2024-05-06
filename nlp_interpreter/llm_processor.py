import json
from langchain_community.llms import Ollama
from schema_validator import is_valid_schema
import llm_switcher

def process_prompt(data, model_name=None, json_schema=None):
    if model_name is None:
        Exception("Model name is required.")
    if json_schema is None:
        Exception("JSON schema is required.")
    prompt = "You are are an expert ontologist and have been asked to help a user define an information extractor.The user will input some text. Based on the user input, you are to provide the json response based on the Provided JSON schema which is" + json_schema+  ". It should be properly divided into the necessary format. And the user input is "+  data + ".Only provide the JSON in the response and nothing else, not even GRAVE ACCENT."
    try:
        nlp_model = llm_switcher.get_nlp_model( model_name=model_name)
    except Exception as e:
        raise ValueError(f"Failed to initialize LLM model: {e}")

    try:
        initial_prompt = prompt
        response =  nlp_model.process_text(initial_prompt)
        if is_valid_schema(response, json_schema):
            return response
        else:
            retry_prompt =  prompt +  ". I want you to provide only the JSON response in the proper format and not " + response
            response =  nlp_model.process_text(retry_prompt)
            if is_valid_schema(response, json_schema):
                return response
            else:
                raise ValueError("Response does not match the JSON schema after retry.")
    except Exception as e:
        return ("The prompt did not return a valid JSON. Please Debug to know more." + str(e) + str(response))  
