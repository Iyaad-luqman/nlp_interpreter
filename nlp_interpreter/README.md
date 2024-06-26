# NLP Interpreter Documentation

## Description

The NLP Interpreter is a  system designed to leverage the power of natural language processing (NLP) to classify textual data into user-defined categories. It offers a flexible and dynamic approach to text analysis, allowing users to specify the categories or actions they are interested in. This system is particularly useful for applications that require the categorization of text into predefined options, enhancing the automation and understanding of textual data.

## Installation
- Install the library 
```bash
pip3 install nlp_interpreter
```
- Add the GEMINI API key to the `.env` file, if you want to use the GEMINI API for text processing and classification.
```bash
GEMINI_API_KEY=your_gemini_api_key
```

## Usage
- The output of all the functions would be json 

- NLP Processing Function to extract custom parameters from the user input.
 
```py
def nlp_process(data):
    json_schema = '''{  "type": "object",  "properties": {    "name": {      "type": "string"  },    "emotion": {      "type": "string"    }  },  "required": [    "name",    "emotion"  ]}'''
    return process_prompt(data, model_name = "llama3", json_schema = json_schema)
```
- NLP Processing Function with GEMINI API
 
```py
def nlp_process(data):
    json_schema = '''{  "type": "object",  "properties": {    "name": {      "type": "string"  },    "emotion": {      "type": "string"    }  },  "required": [    "name",    "emotion"  ]}'''
    return process_prompt(data, model_name = "gemini", json_schema = json_schema)
```

- NLP Classification Function to classify the user input into a single category.
 
```py
def nlp_classify(data):
    options = ["create", "delete", "edit"]
    return classify_prompt(data, model_name = "llama3", options = options)
```

- NLP Classification for Multiple Categories Function to classify the user input into multiple categories.
 
```py
def nlp_classify_into_multiple(data):
    options = ["create", "delete", "edit"]
    return classify_multiple_prompt(data, model_name = "llama3", options = options)
```

## Practical Use Case Example: Smart Home Assistant

### Scenario: Enhancing a Smart Home Assistant with NLP Interpretation

**Background**: Imagine a smart home ecosystem, HomeSmart, that allows users to control various IoT devices through a central assistant. Users can give voice commands to perform actions like adjusting the thermostat, turning lights on or off, playing music, or getting weather updates. However, the assistant's current command recognition system is rigid, requiring users to memorize specific phrases for each action, leading to a less user-friendly experience.

**Solution**: To make the assistant more intuitive and user-friendly, HomeSmart decides to integrate the NLP Interpreter. This integration aims to allow the assistant to understand commands given in natural language, eliminating the need for users to remember specific phrases and making the interaction more conversational.

**Implementation**:
1. **Command Definition**: HomeSmart defines a set of possible actions that the assistant can perform, such as "Adjust Temperature", "Control Lights", "Play Music", and "Weather Update".
2. **NLP Interpreter Integration**: The assistant is integrated with the NLP Interpreter, which is configured to classify user commands into one of the predefined actions based on natural language input.
3. **Dynamic Interaction**: When a user gives a command, the assistant uses the NLP Interpreter to understand the intent and context of the command, mapping it to the corresponding action.
4. **Action Execution**: Once the command is classified, the assistant executes the associated action, such as adjusting the thermostat or turning on the lights.

**Benefits**:
- **Improved User Experience**: Users can interact with the assistant in a more natural and intuitive way, without needing to remember specific command phrases.
- **Flexibility**: The system can easily adapt to new commands or actions as the product evolves, thanks to the dynamic classification capabilities of the NLP Interpreter.
- **Scalability**: The NLP Interpreter can handle a wide range of commands and variations in natural language, making the system robust and scalable.
- **Efficiency**: Automating command interpretation reduces the need for manual updates to the command recognition system, saving time and resources.

**Outcome**: After integrating the NLP Interpreter, HomeSmart notices a significant improvement in user satisfaction. Users find the assistant more responsive and easier to use, leading to increased engagement and usage of the smart home ecosystem. The assistant's ability to understand a wide range of natural language commands also reduces user frustration and enhances the overall smart home experience.

This practical use case demonstrates how the NLP Interpreter can be used to parse natural language input and provide applications with the context needed to take appropriate actions, acting as a bridge between human language and machine-executable commands.



## Use Cases

- **Dynamic Text Classification**: Allows users to define their own categories or options for classification, making the system highly adaptable to various needs.
- **GEMINI API Support**: Offers an alternative to the Ollama model for users who prefer or require GEMINI API for text processing and classification.
- **Content Moderation**: Analyze user-generated content to identify and categorize based on predefined criteria, aiding in moderation efforts.
- **Data Extraction**: Extract specific information from unstructured text inputs for data analysis or entry into structured databases.

## Functionalities

- **User-defined Classification**: Classifies text based on categories or options provided by the user.
- **Multiple Model Support**: Supports both the GEMINI API and the Ollama model for text classification, providing flexibility in choosing the underlying NLP technology.
- **Error Handling**: Implements robust error handling to ensure accurate and reliable classification results.

## Advantages

- **Customizability**: Users can define their own categories, making the system highly adaptable.
- **Flexibility**: Supports multiple NLP backends (GEMINI API and Ollama model), allowing users to choose the one that best fits their needs.
- **Ease of Integration**: The Flask-based API facilitates easy integration into existing systems or workflows.

## Error Handling

The system includes comprehensive error handling to ensure the accuracy of classifications. It checks the NLP model's response to ensure it aligns with the user-defined criteria. In cases where the response does not meet these criteria, the system can modify the prompt and retry or provide informative errors, enhancing reliability even in complex scenarios.

### Types of Cases It Can Handle:

- **Valid Responses**: Directly returns the model's response if it aligns with the user-defined criteria.
- **Invalid Responses**: Attempts to guide the model towards a valid output by modifying the prompt and retrying.
- **Error Conditions**: Provides detailed error messages if issues arise during model initialization or if the response does not meet the criteria after retries.

