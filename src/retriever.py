from langchain_community.vectorstores import Chroma


def get_retriever(vector_store: Chroma,k:int=4):
    """
    Creates and returns a retriever from the given Chroma vector store.
    """
    retriever = vector_store.as_retriever(search_type="mmr",
        search_kwargs={"k": k, "fetch_k": 20})
    
    return retriever