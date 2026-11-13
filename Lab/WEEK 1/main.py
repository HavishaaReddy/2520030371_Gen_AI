from dotenv import load_dotenv
from google import genai
import os

# Step 1: Load API key from .env
load_dotenv()

# Step 2: Read Gemini API key
api_key = os.getenv("GEMINI_API_KEY")
if not api_key:
    raise ValueError("Gemini API key not found!")
print("1. API key loaded.", flush=True)

# Step 3: Initialize Gemini client
client = genai.Client(api_key=api_key)
print("2. Sending prompt to Gemini...", flush=True)

# Step 4: Make first LLM call
response = client.models.generate_content(
    model="gemini-3.8-flash",
    contents="What is Artificial Intelligence? Explain in simple words."
)

# Step 5: Display response
print("\nLLM Response:")
print(response.text)