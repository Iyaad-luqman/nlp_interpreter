from setuptools import setup, find_packages

setup(
    name='nlp_interpreter',
    version='1.0.0',
    description='A package for translating Natural language using NLP processing with Ollama and Gemini into actions.',
    author='Iyaad Luqman K',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/Iyaad-luqman/nlp_interpreter',
    license='MIT',
    author_email='iyaadluq@gmail.com',
    packages=find_packages(),
    install_requires=[
        'langchain_community',
        'python-dotenv',
        'google-generativeai',
        'jsonschema'
    ],
)