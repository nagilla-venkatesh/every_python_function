import os

import openai
from constants import OPENAI_API_KEY

PROMPT = "An eco-friendly computer from the 90s in the style of vaporwave"

openai.api_key = OPENAI_API_KEY

response = openai.Image.create(
    prompt=PROMPT,
    n=3,
    size="256x256",
    response_format="b64_json",
)

print(response["data"][0]["b64_json"][:50])




