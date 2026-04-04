from groq import Groq

client = Groq(api_key="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")

# Memory
messages = [
    {"role": "system", "content": "You are a helpful AI assistant."}
]

# Tool 1: Calculator
def calculator(query):
    try:
        return str(eval(query))
    except:
        return "Calculation error"

while True:
    user_input = input("You: ")

    if user_input.lower() == "exit":
        break

    # Store user input
    messages.append({"role": "user", "content": user_input})

    # Decision making (agent logic)
    if any(op in user_input for op in ["+", "-", "*", "/"]):
        tool_result = calculator(user_input)
        print("🧮 Tool:", tool_result)

        # Add tool result to memory
        messages.append({"role": "assistant", "content": tool_result})
    else:
        # Use LLM
        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=messages
        )

        reply = response.choices[0].message.content
        print("🤖 AI:", reply)

        # Save response
        messages.append({"role": "assistant", "content": reply})