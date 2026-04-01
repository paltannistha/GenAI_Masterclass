# 🌟 Day 2: Hands-on with GenAI & Intro to Agentic AI

## 📌 Overview
This session focuses on **prompting techniques** and a **basic understanding of Agentic AI** with simple examples.

---

## 🔁 Quick Recap
- **GenAI** → Generates content  
- **Agentic AI** → Takes actions  
- Based on **LLMs + Prompts**

---

## ✍️ What is Prompting?
A **prompt** is the input you give to an AI model.

👉 Output quality depends on how clearly you ask.

### Example:
- ❌ Bad: `Tell me about AI`  
- ✅ Better: `Explain AI in 3 lines for beginners`

---

# 🧠 Types of Prompts in GenAI

## 📌 Overview
Prompts are the inputs given to a Generative AI model.  
Different types of prompts help guide the AI to produce **more accurate and useful outputs**.


---

## ✨ 1. Simple Prompt
A basic instruction without much detail.

### Example:
**Write a poem on nature**

👉 Used for general or creative tasks.

---

## 📋 2. Instruction-based Prompt
A clear instruction with a specific format or requirement.

### Example:
**Explain cloud computing in 5 bullet points**

👉 Helps control the **structure of the output**.

---

## 🎭 3. Role-based Prompt
Assigns a role to the AI to shape the response style.

### Example:
**You are a teacher. Explain AI to a 10-year-old.**

👉 Improves **tone, clarity, and audience targeting**.

---

## 📚 4. Context-based Prompt
Provides background information before asking the question.

### Example:
**I am preparing for an interview. Explain REST APIs simply.**

👉 Produces **more relevant and personalized answers**.

---

👉 **Key Idea:** More clarity = better output

---

## 🧪 Mini Hands-on

### Task 1: Improve Output

**Basic Prompt:**

Tell me about Python

**Improved Prompt:**

Explain Python in 5 points with real-life examples

---

### Task 2: Role-based Prompt
You are a coding mentor. Explain loops in simple terms.


---

## 🤖 Intro to Agentic AI

### Without Agent
- User asks → AI answers  

### With Agent
- AI thinks → plans → acts  

### Example Flow:
1. User: “Book me a flight”  
2. AI:
   - Searches flights  
   - Compares options  
   - Suggests best choice  

---

## ⚙️ Agent Components

- **Brain (LLM)** → Thinking  
- **Tools** → APIs, search, calculator  
- **Memory** → Stores context  
- **Planner** → Decides steps  

---

## 💻 Simple Agent Example (Conceptual)

```python
user_input = "Find best laptop under 50000"

# Step 1: Understand
intent = "search product"

# Step 2: Use tool
results = search_api(user_input)

# Step 3: Decide
best = choose_best(results)

# Step 4: Output
print(best)

```

👉 **Agents can perform actions, not just generate text.**

---

## 🌍 Real Use Cases

- AI email automation  
- Customer support bots  
- Personal assistants (booking, reminders)  

---

## ✅ Key Takeaways

- Prompting is very important  
- Better prompts → better outputs  
- Agentic AI = AI + decision-making + actions  

---

## 🚀 What's Next?

- Build your first GenAI application  
- Explore tools like APIs and integrations  
- Move towards creating your own AI agent  
