WEEK 3 - LLM Monitoring System

This experiment demonstrates monitoring and logging of LLM API usage using Gemini/Ollama and MongoDB.
The application sends a user prompt to an LLM, generates a response, measures latency and token usage, estimates cost, and stores the usage details in MongoDB for tracking.

Files: main.py, llm_client.py, usage_logger.py, test_client.py, test_mongodb.py, requirements.txt.

Requirements: Python 3.14, MongoDB Atlas, Gemini API Key, Ollama 

Setup:
1. Install dependencies using pip install -r requirements.txt
2. Configure the .env file with the Gemini API key and MongoDB URI
3. Download the Ollama model using ollama pull llama3.2

Run: python main.py

Sample Prompt: What is Artificial Intelligence?
