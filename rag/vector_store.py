from langchain_community.document_loaders import DirectoryLoader, TextLoader
from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import HuggingFaceEmbeddings

DOCUMENTS_PATH = "rag/documents"
DB_PATH = "rag/chroma_db"

def create_vector_store():

    # Load all txt files
    loader = DirectoryLoader(
        DOCUMENTS_PATH,
        glob="*.txt",
        loader_cls=TextLoader
    )

    documents = loader.load()

    print(f"Loaded {len(documents)} documents")

    # Create embeddings model
    embeddings = HuggingFaceEmbeddings(
        model_name="all-MiniLM-L6-v2"
    )

    # Create vector database
    vector_db = Chroma.from_documents(
        documents=documents,
        embedding=embeddings,
        persist_directory=DB_PATH
    )

    print("Vector database created successfully")

    return vector_db

if __name__ == "__main__":
    create_vector_store()