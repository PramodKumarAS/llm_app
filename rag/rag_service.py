from rag.retriever import retrieve_context
from llm.llm_client import ask_llm

def ask_rag(question: str):

    context = retrieve_context(question)
    if context is None:
       return ask_llm([
         {"role": "user", "content": question}
    ])

    prompt = f"""
    Answer using only the provided context.

    Context:
    {context}

    Question:
    {question}
    """

    messages = [
        {
            "role": "user",
            "content": prompt
        }
    ]

    return ask_llm(messages)