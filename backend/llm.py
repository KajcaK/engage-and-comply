#!/usr/bin/env python3

from openai import OpenAI
import os

client = OpenAI(
  base_url="https://api.featherless.ai/v1",
  api_key=os.getenv("FEATHERLESS_API_KEY"),
)

SYSTEM_PROMPT = """
You are an AI teacher assistant for a resource that helps employees learn about ecological compliance.
After the user says "Start", you will pick
"""

response = client.chat.completions.create(
  model='meta-llama/Meta-Llama-3.1-8B-Instruct',
  messages=[
    {"role": "system", "content": "You are a helpful assistant."},
    {"role": "user", "content": "Hello!"}
  ],
)
print(response.model_dump()['choices'][0]['message']['content'])
