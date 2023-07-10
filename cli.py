#!/usr/bin/env python3
import sys
from sdxl import generate_image

prompt = sys.argv[1]
print(f"Generating image for prompt: {prompt} ...")
generate_image(prompt)