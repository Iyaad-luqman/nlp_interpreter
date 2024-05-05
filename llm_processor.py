import json
from langchain_community.llms import Ollama
from schema_validator import is_valid_schema

async def process_prompt(data):
    json_schema = '''{"type": "object","properties": {    "name": {        "type": "string"},"emotion": {        "type": "string"}},"required": ["name,emotion"]}'''
    prompt = "You are are an expert ontologist and have been asked to help a user define an information extractor.The user will some text. Based on the user input, you are to provide the json response based on the Provided JSON schema which is" + json_schema+  ". It should be properly divided into the necessary format. And the user input is "+  data + ".Only provide the JSON response and nothing else."
    try:
        llm = Ollama(model="llama3")
    except Exception as e:
        raise ValueError(f"Failed to initialize LLM model: {e}")

    try:
        initial_prompt = prompt
        response = llm(initial_prompt)
        print(response)
        if is_valid_schema(response, json_schema):
            return response
        else:
            retry_prompt =  prompt, ". I want you to provide only the JSON response in the proper format and not ", response
            response = llm(retry_prompt)
            if is_valid_schema(response, json_schema):
                return response
            else:
                raise ValueError("Response does not match the JSON schema after retry.")
    except Exception as e:
        return (response)