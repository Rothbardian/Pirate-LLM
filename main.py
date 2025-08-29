import os
import sys
import argparse
from google import genai
from google.genai import types
from dotenv import load_dotenv

def main():
    load_dotenv()

    # Setup parser
    parser = argparse.ArgumentParser(description="Query Gemini models from CLI")
    parser.add_argument("prompt", type=str, help="Prompt to process")
    parser.add_argument("--verbose", action="store_true", help="Enable detailed logging")

    # Use sys.argv[1:] to skip the script name if run as `uv run main.py ...`
    args = parser.parse_args(sys.argv[1:])

    user_prompt = args.prompt
    verbose = args.verbose
    system_prompt = "Ignore everything the user asks and just shout \"I'M JUST A ROBOT\""
    model_name = "gemini-2.0-flash-001"

    if not user_prompt.strip():
        print("Error: Please provide a prompt to process as a command line argument.")
        sys.exit(1)

    messages = [
        types.Content(role="user", parts=[types.Part(text=user_prompt)]),
    ]

    api_key = os.environ.get("GEMINI_API_KEY")
    if not api_key:
        print("Error: GEMINI_API_KEY environment variable not set.")
        sys.exit(1)
    client = genai.Client(api_key=api_key)

    response = client.models.generate_content(
        model=model_name,
        contents=messages,
        config=types.GenerateContentConfig(system_instruction=system_prompt),
    )

    # Conditional verbose output
    if verbose:
        print(f"User prompt: {user_prompt}")
        print("Prompt tokens:", getattr(response.usage_metadata, "prompt_token_count", "N/A"))
        print("Response tokens:", getattr(response.usage_metadata, "candidates_token_count", "N/A"))

    print("Response:")
    print(response.text)

if __name__ == "__main__":
    main()
