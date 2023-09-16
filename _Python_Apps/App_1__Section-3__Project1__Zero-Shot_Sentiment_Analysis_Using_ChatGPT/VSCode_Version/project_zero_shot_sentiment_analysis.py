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

'''
# Test 1: Basic Tests
emotions = 'positive, negative'
prompt = 'AI will take over the world.'

print(gpt_classify_sentiment(prompt, emotions))


emotions = "happy, sad, angry, mad, tired, very happy, very sad, very angry, very tired, very mad"
prompt = 'I lost my phone.'

print(gpt_classify_sentiment(prompt, emotions))


emotions = "happy, sad, angry, mad, tired, very happy, very sad, very angry, very tired, very mad"
prompt = 'AI will take over the world and destroy the human race.'
prompt = 'I am going to sleep.'
prompt = "Let's take a break! I can't do it anymore!"
prompt = 'The company CEO just missed out a $10 million bonus, but he still got a raise.'
prompt = '😀'
prompt = 'ಠ_ಠ'
prompt = '😠'

print(gpt_classify_sentiment(prompt, emotions))
'''

# Test 2: Review Classifier
emotions = 'positive, negative'
review = '''Super explanation with all the important things you have to know in Python.
The course has a lot of examples and exercises.
Part 2 contains a lot of Python projects and shows you how to use Python in real-world scenarios.
'''
emotion = gpt_classify_sentiment(review, emotions)
print(f'{review[:50]} ... ======> {emotion.upper()}')


emotions = 'positive, negative'
review = '''This wasn't a good match for me and doesn't fit my learning style.'''
emotion = gpt_classify_sentiment(review, emotions)
print(f'{review[:50]} ... ======> {emotion.upper()}')


# Test 3: Fake News Detector
emotions = 'True, False'
prompt = 'The moon landings were all faked.'
emotion = gpt_classify_sentiment(prompt, emotions)
print(f'{prompt} ====> {emotion.upper()}')


prompt = 'The earth is flat.'
emotion = gpt_classify_sentiment(prompt, emotions)
print(f'{prompt} ====> {emotion.upper()}')

prompt = 'Elvis Presley died in 1977.'
emotion = gpt_classify_sentiment(prompt, emotions)
print(f'{prompt} ====> {emotion.upper()}')

prompt = 'Quantum entanglement has been experimentally demonstrated with photons, electrons, and other particles.'
emotion = gpt_classify_sentiment(prompt, emotions)
print(f'{prompt} ====> {emotion.upper()}')




