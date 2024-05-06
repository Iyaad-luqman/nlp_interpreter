from setuptools import setup, find_packages

setup(
    name='nlp_interpreter',
    version='0.1.0',
    description='A package for translating Natural language using NLP processing with Ollama and Gemini into actions.',
    author='Iyaad Luqman K',
    author_email='iyaadluq@gmail.com',
    packages=find_packages(),
    install_requires=[
        'langchain_community',
        'python-dotenv',
        'google-generativeai',
        'jsonschema'
    ],
)