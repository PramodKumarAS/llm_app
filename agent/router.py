from llm.llm_client import ask_llm
import json

def choose_tool(question):

    prompt = f"""
You are a routing agent.

Available tools:

1. weather
   - Current weather information

2. rag
   - Company policy questions

3. calculator
   - Mathematical calculations

4. stock
   - Stock prices

Return ONLY valid JSON.

Examples:

Question: What is the weather in Bangalore?
{{"tool":"weather","city":"Bangalore"}}

Question: Who gets health insurance?
{{"tool":"rag"}}

Question: What is 25 * 40?
{{"tool":"calculator","expression":"25*40"}}

Question: Calculate (100 + 50) / 5
{{"tool":"calculator","expression":"(100+50)/5"}}

Question: What is Apple's stock price?
{{"tool":"stock","symbol":"AAPL"}}

Question:
{question}
"""

    response = ask_llm(
        [
            {
                "role": "user",
                "content": prompt
            }
        ]
    )
    return json.loads(response)