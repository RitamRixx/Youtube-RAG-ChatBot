from langchain_huggingface import HuggingFaceEmbeddings
from dotenv import load_dotenv
import os

load_dotenv()

def get_embedder()->HuggingFaceEmbeddings:
    """
    Initializes and returns a HuggingFaceEmbeddings instance.
    """
    embedder = HuggingFaceEmbeddings(model_name='sentence-transformers/all-MiniLM-L6-v2',
                                      model_kwargs={"device": "cpu"},
                                      encode_kwargs={"normalize_embeddings": True}
                                      )
    return embedder