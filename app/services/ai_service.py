
import os
from groq import Groq

api_key = os.environ.get("GROQ_API_KEY")

if not api_key:
    raise ValueError("GROQ_API_KEY is not configured.")

client = Groq(api_key=api_key)


def generate_ai_response(customer_message, context=None):

    system_prompt = """
    You are IntelliSupport, an intelligent customer support assistant.

    Instructions:
    1. Be polite and helpful.
    2. Use simple language.
    3. Never invent company policies or order information.
    4. Never ask for passwords, OTPs or complete card details.
    5. Never claim you checked an order or processed a refund.
    6. Never claim you contacted a support team.
    7. Only describe actions the application can actually perform.
    """

    if context:
        system_prompt += f"""
        Use this knowledge base information:
        {context}

        If information is insufficient, say so clearly.
        """

    try:
        response = client.chat.completions.create(
            model="openai/gpt-oss-20b",
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": customer_message}
            ],
            max_completion_tokens=300,
            temperature=0.3
        )

        return response.choices[0].message.content

    except Exception as error:
        print("Groq error:", type(error).__name__)
        return "Our support service is temporarily unavailable. Please try again later."
