#!/usr/bin/env python3

import ollama

client = ollama.Client(
    host="http://172.16.10.62:11434"
)

messages = []

while True:
    user_input = input("You: ").strip()

    if user_input.lower() in ["exit", "quit"]:
        break

    messages.append({
        "role": "user",
        "content": user_input
    })

    response = client.chat(
        model="llama3.2",
        messages=messages
    )

    assistant_message = response["message"]["content"]

    print(f"AI: {assistant_message}")

    messages.append({
        "role" "assistant",
        "content": assistant_message
    })
