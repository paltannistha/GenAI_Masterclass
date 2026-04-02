from groq import Groq

# 👉 Replace with your actual API key
client = Groq(api_key="YOUR API Key")

# Store conversation (memory)
messages = [
    {"role": "system", "content": "You are a helpful assistant who explains things simply."}
]

print("🤖 AI Chatbot (type 'exit' to quit)\n")

while True:
    # Take user input
    user_input = input("You: ")

    if user_input.lower() == "exit":
        print("👋 Exiting chatbot...")
        break

    # Add user message to history
    messages.append({"role": "user", "content": user_input})

    # Send request to Groq
    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=messages
    )

    # Extract reply
    reply = response.choices[0].message.content

    # Print response
    print("AI:", reply, "\n")

    # Save AI response to memory
    messages.append({"role": "assistant", "content": reply})