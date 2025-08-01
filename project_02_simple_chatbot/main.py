# main.py
# Objective: Create a basic interactive chatbot that takes user input.

from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
import os

load_dotenv()
google_api_key = os.getenv("GEMINI_API_KEY")
model = "gemini-2.5-flash-lite"

def run_simple_chatbot():
    """
    Continuously prompts the user for input, feeds it to the LLM, and prints the response.
    Exits when the user types 'quit'.
    """
    llm = ChatGoogleGenerativeAI(model=model, google_api_key=google_api_key)

    print("Simple Chatbot. Type 'quit' to exit.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'quit':
            break
        response = llm.invoke(user_input)
        print(f"Bot: {response.content}")

if __name__ == "__main__":
    run_simple_chatbot()
