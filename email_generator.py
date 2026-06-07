import ollama

def generate_email(prompt):
    response = ollama.chat(
        model="gemma4:e4b",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return response["message"]["content"]