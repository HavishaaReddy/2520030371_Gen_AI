Week 2 - Provider Agnostic LLM Client

This experiment provides a common interface for interacting with different LLM providers. 
We can choose either Gemini or Ollama and generate responses.

Requirements: Python 3.14+, Gemini API Key, Ollama

Setup:
1. pip install -r requirements.txt
2. ollama pull llama3.2
3. Add your Gemini API key in the .env file.

Run: python main.py

Sample Prompt: What are the applications of Artificial Intelligence?
