from llm.llm_client import ask_llm


def ask_chat(question):

    messages = [
        {
            "role": "user",
            "content": question
        }
    ]
    
    return ask_llm(messages)