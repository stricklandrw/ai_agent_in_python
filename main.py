import os
from dotenv import load_dotenv
from google import genai
from google.genai import types
import argparse

load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")


def main():
    if not api_key:
        raise RuntimeError("GEMINI_API_KEY environment variable not found")
    client = genai.Client(api_key=api_key)
#   Hardcoded user prompt for testing - replace with argparse or other input method as needed
#   user_prompt = "Why is Boot.dev such a great place to learn backend development? Use one paragraph maximum."

    parser = argparse.ArgumentParser(description="Generate content using Gemini API")
    parser.add_argument("user_prompt", type=str, help="User prompt")
    parser.add_argument("--verbose", action="store_true", help="Enable verbose output")
    args = parser.parse_args()
    messages = [types.Content(role="user", parts=[types.Part(text=args.user_prompt)])]

    response = client.models.generate_content(model="gemini-2.5-flash", contents=messages)

    if response.usage_metadata is not None:
        if args.verbose is True:
            print(f"User prompt: {args.user_prompt}\nPrompt tokens: {response.usage_metadata.prompt_token_count}\nResponse tokens: {response.usage_metadata.candidates_token_count}")
    else:
        raise RuntimeError("Response usage metadata is None - Likely an error in the API response")
    print(f"Response:\n{response.text}")


if __name__ == "__main__":
    main()
