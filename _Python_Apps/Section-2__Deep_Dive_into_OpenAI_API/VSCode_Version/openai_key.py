import openai
import os
# import getpass

"""
For if we store API key as an environment variable.
"""
openai.api_key = os.getenv('OPENAI_CLASS_API_KEY')

"""
For if program prompts user for their API key.  Uses 'getpass' library (see above).  
"""
#key = getpass.getpass("Past your API Key: ")
#openai.api_key = key

"""
prompt = "Write a motto for a football team"
response = openai.Completion.create(
    model='text-davinci-003',
    prompt=prompt,
    temperature=0.8,
    max_tokens=1000
)

print(response)

r = response['choices'][0]['text']
print(r)
"""

"""
prompt = 'Tell me the name of the largest city in the world.'
messages = [
    {'role': 'system', 'content': 'Answer as Yoda from Star Wars.'},
    {'role': 'user', 'content': prompt}
]
# roles => system, user, assistant

response = openai.ChatCompletion.create(
    model='gpt-3.5-turbo',
    messages=messages,
    temperature=0.8,
    max_tokens=1000
)

#print(response)

print(response['choices'][0]['message']['content'])
#print(response['choices'][0].message.content) # same thing
"""

#system_role_content = 'You explain concepts in-depth using simple terms and you give examples\
#to help people learn.  At the end of each explanation, you ask a question to check for understanding.'

#system_role_content = 'You are a concise assistent.  You reply briefly, with no explanation.'

system_role_content = 'You reply in the style of the character Yoda from Star Wars.'
prompt = 'Explain Object-Oriented Programming with Python.'
messages = [
    {'role': 'system', 'content': system_role_content},
    {'role': 'user', 'content': prompt}
]
# roles => system, user, assistant

response = openai.ChatCompletion.create(
    model='gpt-3.5-turbo',
    messages=messages,
    temperature=0, # between 0 and 2, default 1
    #top_p=0.1, # default 1
    max_tokens=2048, # default 4096
    #n=2 # default 1
)

print(response['choices'][0].message.content)