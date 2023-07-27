# !pip install -q openai, requests
import openai
import os
import requests
import shutil
from PIL import Image

openai.api_key = os.getenv('OPENAI_CLASS_API_KEY')

image_prompt = 'Man on a motorcycle on a cyberpunk street, high quality photography.'

response = openai.Image.create(
    prompt=image_prompt,
    n=1,
    size='1024x1024'
)

#print(response)
image_url = response['data'][0]['url']
print(image_url)

resource = requests.get(image_url, stream=True)

#print(resource.status_code)

if resource.status_code == 200:
    with open('dalle1.png', 'wb') as f:
        shutil.copyfileobj(resource.raw, f)
else:
    print('Error accessing the image!')

Image.open('dalle1.png')