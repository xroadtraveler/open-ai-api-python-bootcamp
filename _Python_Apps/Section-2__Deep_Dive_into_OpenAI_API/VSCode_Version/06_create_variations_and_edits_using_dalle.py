import openai
import os

openai.api_key = os.getenv('OPENAI_CLASS_API_KEY')

image = open('original.png', 'rb')
response = openai.Image.create_variation(
    image=image,
    n=1,
    size='1024x1024'
)

image_url = response['data'][0]['url']


## Edit Images

image = open('motorcycle_original.png', 'rb')
mask = open('mask.png', 'rb')
response = openai.Image.create_edit(
    image=image,
    mask=mask,
    prompt='John Wick riding a motorcycle on an apocalyptic field containing a big red moon \
    with a cyberpunk look, high quality photography',
    n=1,
    size='1024x1024'
)

image_url = response['data'][0]['url']
print(image_url)




