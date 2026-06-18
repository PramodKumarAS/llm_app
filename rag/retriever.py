from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import HuggingFaceEmbeddings
from dotenv import load_dotenv

load_dotenv()
DB_PATH = "rag/chroma_db"

embeddings = OpenAIEmbeddings(
    model="text-embedding-3-small"
)

vector_db = Chroma(
    persist_directory=DB_PATH,
    embedding_function=embeddings
)

retriever = vector_db.as_retriever()


def retrieve_context(question):

    results = vector_db.similarity_search_with_score(
        question,
        k=3
    )

    best_doc, best_score = results[0]

    if best_score > 1.2:
        return None
    
    return best_doc.page_content
    # return "\n\n".join(
    #     doc.page_content
    #     for doc, score in results
    # )
