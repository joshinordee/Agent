import os
from dotenv import load_dotenv
from google import genai
import sys
from google.genai import types

load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")

client = genai.Client(api_key=api_key)

def is_verbose(args): # check for verbose argument in command line
    return "--verbose" in args

def main():
    excluded_strings = ["main.py", "--verbose"]
    prompt_args = list(filter(lambda x: x not in excluded_strings, sys.argv)) # filter out user prompt from sys argument 

    if not prompt_args:
        print("Error. Must enter string prompt.")
        sys.exit(1)
    user_prompt = prompt_args[0]

    messages = [types.Content(role="user", parts=[types.Part(text=user_prompt)]),]
    response = client.models.generate_content(model='gemini-2.0-flash-001', contents=messages)

    if is_verbose(sys.argv):
        print(f"User prompt: {user_prompt}") 
        print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
        print(f"Response tokens: {response.usage_metadata.candidates_token_count}")
    print(response.text)
    




if __name__ == "__main__":
    main()
