import openai
import os

"""
with open('key.txt', 'r') as f:
    api_key = f.read().strip('\n')
    assert api_key.startswith('sk-'), 'Error loading the API key. The API key starts with "sk-"'
openai.api_key = api_key
"""

openai.api_key = os.getenv('OPENAI_CLASS_API_KEY')