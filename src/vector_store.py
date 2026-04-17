from langchain_community.vectorstores import Chroma
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_core.documents import Document
from typing import List

VECTOR_STORE_DIR = "./vector_store"


def build_vector_store(chunks: List[Document], embedder: HuggingFaceEmbeddings) -> Chroma:
    vector_store = Chroma.from_documents(
        documents=chunks,
        embedding=embedder,
        persist_directory=VECTOR_STORE_DIR
    )
    return vector_store


def load_vector_store(embedder: HuggingFaceEmbeddings) -> Chroma:
    """Loads a previously saved Chroma DB from disk."""
    return Chroma(
        persist_directory=VECTOR_STORE_DIR,
        embedding_function=embedder
    )