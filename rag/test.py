import os
import glob
from dotenv import load_dotenv
from pathlib import Path
import gradio as gr
from openai import OpenAI

# setting up
load_dotenv(override=True)

open_api_key = os.getenv("OPENAI_API_KEY")
ollama_base_url = os.getenv("OLLAMA_BASE_URL")
ollama_api_key = os.getenv("OLLAMA_API_KEY")

if open_api_key:
  print("key found")
else:
  print("Key not found")

MODEL = "gpt-4.1-nano"
openAI = OpenAI()

# Read data
knowledge = {}
filenames = glob.glob("knowledge-base/employees/*")

for filename in filenames:
    name = Path(filename).stem.split(' ')[-1]
    with open(filename, "r", encoding="utf-8") as f:
        knowledge[name.lower()] = f.read()

print(knowledge)