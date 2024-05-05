from llm_processor import process_prompt
from llm_classifier import classify_prompt

def process(data: str):
    try:
        response_json = process_prompt(data)
        return response_json
    except ValueError as ve:
        print(f"ValueError: {str(ve)}")
        return None
    except Exception as e:
        print("An unexpected error occurred.")
        return None
    
def classify(data: str):
    try:
        response_json = classify_prompt(data)
        return response_json
    except ValueError as ve:
        print(f"ValueError: {str(ve)}")
        return None
    except Exception as e:
        print("An unexpected error occurred.")
        return None