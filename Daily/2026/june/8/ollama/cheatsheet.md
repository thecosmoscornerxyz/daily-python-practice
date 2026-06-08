# LIST OLLAMA MODELS #

import ollama

print(ollama.list())

# FIRST OLLAMA PROMPT #

import ollama

response = ollama.chat(model="llama3.2", messages=[{"role": "user", "content": "Hello, World!"}])
print(response["message"]["content"])

# OLLAMA GENERATE PROMPT #

import ollama

result = ollama.generate(model="llama3.2", prompt="Explain what a CPU does in one sentence")
print(result["response"])

