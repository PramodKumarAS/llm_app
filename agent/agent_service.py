from agent.router import choose_tool
from agent.tools import get_weather, calculate, get_stock_price
from rag.rag_service import ask_rag
from chat.chat_service import ask_chat

def ask_agent(question):

    decision = choose_tool(question)

    tool = decision["tool"]

    if tool == "weather":

        weather = get_weather(
            decision["city"]
        )

        response = (
            f"{weather['city']} is "
            f"{weather['temperature']}°C "
            f"with {weather['description']}."
        )

    elif tool == "rag":
        response = ask_rag(question)

    elif tool == "calculator":
        response = str(
            calculate(
                decision["expression"]
            )
        )

    elif tool == "stock":
     try:

        stock = get_stock_price(
            decision["symbol"]
        )

        if stock["price"] == "temporarily unavailable":
            response = (
                f"Unable to retrieve {stock['symbol']} "
                f"stock price at the moment."
            )
        else:
            response = (
                f"{stock['symbol']} is trading at "
                f"${stock['price']}"
            )
            
     except Exception:
        response = (
            "Unable to retrieve stock price "
            "at the moment."
        )            

    else:
        response = ask_chat(question)

    return {
        "tool_used": tool,
        "decision": decision,
        "response": response
    }