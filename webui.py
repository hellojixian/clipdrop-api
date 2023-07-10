#!/usr/bin/env python
import os, sys
import gradio as gr
from sdxl import generate_image
from dotenv import load_dotenv
load_dotenv()

SERVER_PORT = os.environ.get("SERVER_PORT", '8000')
SERVER_HOST = os.environ.get("SERVER_HOST", 'localhost')

def generate_task(input_text):
  # Generate HTML code dynamically based on the input
  image = generate_image(input_text)
  html_code = f"<h2>Prompts:</h2>"
  html_code += f"<p>{input_text}</p>"
  html_code += f"<h2>Generated Image:</h2>"
  html_code += f"<p><img src='file/{image}'/></p>"
  return html_code

webapp = gr.Interface(
  title="Generate Image with SDXL 0.9",
  inputs=[gr.components.Textbox(lines=1,
                                placeholder="Please enter text prompt here",
                                label="Text",)],
  fn=generate_task,
  outputs="html",
  allow_flagging='never',
)

# print(webapp)
webapp.launch(server_name=str(SERVER_HOST),
           server_port=int(SERVER_PORT))