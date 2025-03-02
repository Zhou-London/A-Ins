"""
Configuration of OpenAI API
"""

from openai import OpenAI

from dotenv import load_dotenv
import os

load_dotenv()

key = os.getenv("OPENAI_KEY")

if key is None:
    raise KeyError("OpenAI Key not found/invalid.")

openai_client = OpenAI(api_key=key)
