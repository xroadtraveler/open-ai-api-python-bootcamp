import openai
import os

"""
with open('key.txt', 'r') as f:
    api_key = f.read().strip('\n')
    assert api_key.startswith('sk-'), 'Error loading the API key. The API key starts with "sk-"'
openai.api_key = api_key
"""

openai.api_key = os.getenv('OPENAI_CLASS_API_KEY')

def gpt_classify_sentiment(prompt, emotions):
    system_prompt = f'''You are an emotionally intelligent assistant.
    Classify the sentiment of the user's text with ONLY ONE OF THE FOLLOWING EMOTIONS: {emotions}.
    After classifying the text, respond with the emotion ONLY.
    '''
    
    response = openai.ChatCompletion.create(
        model='gpt-3.5-turbo',
        messages=[
            {'role': 'system', 'content': system_prompt},
            {'role': 'user', 'content': prompt}
        ],
        max_tokens=20,
        temperature=0
    )
    
    r = response['choices'][0].message.content
    if r == '':
        r = 'N/A'
        
    return r