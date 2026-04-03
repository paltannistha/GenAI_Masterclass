from groq import Groq

client = Groq(api_key="YOUR_API_KEY")

def calculator(query):
    try:
        return str(eval(query))
    except:
        return "Error in calculation"

while True:
    user_input = input("You: ")

    if user_input.lower() == "exit":
        break

    # Simple decision (agent behavior)
    if any(op in user_input for op in ["+", "-", "*", "/"]):
        result = calculator(user_input)
        print("Tool:", result)
    else:
        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[{"role": "user", "content": user_input}]
        )
        print("AI:", response.choices[0].message.content)