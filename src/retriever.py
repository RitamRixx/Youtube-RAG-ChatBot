from langchain_community.vectorstores import Chroma


def get_retriever(vector_store: Chroma,k:int=4):
    """
    Creates and returns a retriever from the given Chroma vector store.
    """
    retriever = vector_store.as_retriever(search_type="similarity",
        search_kwargs={"k": k})
    
    return retriever