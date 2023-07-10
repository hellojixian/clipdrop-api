import requests
import os
from dotenv import load_dotenv
load_dotenv()

def generate_image(prompt: str):
  api_key = os.getenv('CLIPDROP_API_KEY')
  filename = 'output/generated_image.png'
  r = requests.post('https://clipdrop-api.co/text-to-image/v1',
    files = {
        'prompt': (None, prompt, 'text/plain')
    },
    headers = { 'x-api-key': api_key}
  )
  if (r.ok):
    # r.content contains the bytes of the returned image
    image = r.content
    # save image bytes to file

    with open(filename, 'wb') as f:
      f.write(image)
  else:
    r.raise_for_status()

  return filename
