import os
from dotenv import load_dotenv
from google import genai

load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")


def main():
    if not api_key:
        raise RuntimeError("GEMINI_API_KEY environment variable not found")
    client = genai.Client(api_key=api_key)
    user_prompt = "Why is Boot.dev such a great place to learn backend development? Use one paragraph maximum."

    response = client.models.generate_content(model="gemini-2.5-flash", contents=user_prompt)

    print(f"User prompt: {user_prompt}")
    if response.usage_metadata is not None:
        print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}\nResponse tokens: {response.usage_metadata.candidates_token_count}")
    else:
        raise RuntimeError("Response usage metadata is None - Likely an error in the API response")
    print(f"Response:\n{response.text}")


if __name__ == "__main__":
    main()
