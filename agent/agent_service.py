from agent.router import choose_tool
from agent.tools import get_weather, calculate, get_stock_price
# from rag.rag_service import ask_rag


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
        return "RAG temporarily disabled"
        # response = ask_rag(question)

    elif tool == "calculator":

        response = str(
            calculate(
                decision["expression"]
            )
        )

    elif tool == "stock":

        stock = get_stock_price(
            decision["symbol"]
        )

        response = (
            f"{stock['symbol']} "
            f"is trading at "
            f"${stock['price']}"
        )

    else:

        response = "Unable to determine tool."

    return {
        "tool_used": tool,
        "decision": decision,
        "response": response
    }