from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv() #by default looks for the .env file in the current directory

client = OpenAI(
    base_url = os.getenv("BASE_URL"),
    api_key = os.getenv("API_KEY")
)

while True:
    input_text = input("\nYou: ")

    if input_text.lower() in ["exit","bye","quit"]:
        print("Exiting the chat. Goodbye!")
        break

    response = client.chat.completions.create(
        model=os.getenv("MODEL"),
        messages=[
            {
                "role": "user",
                "content":input_text
            }
        ],
        max_completion_tokens=20
    )

    print("\nLLM Response:")
    print(response.choices[0].message.content)
    print(response.choices[0].message.role)