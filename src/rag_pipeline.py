import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.runnables import RunnablePassthrough,RunnableParallel,RunnableLambda
from langchain_core.output_parsers import StrOutputParser
from langchain_core.documents import Document
from typing import List


from src.loader import get_transcript
from src.splitter import split_transcript
from src.embedder import get_embedder
from src.vector_store import build_vector_store
from src.retriever import get_retriever
from src.prompt_template import get_rag_prompt


load_dotenv()

llm = ChatOpenAI(
    model="openai/gpt-4o-mini",
    openai_api_key=os.getenv("OPENROUTER_API_KEY"),
    openai_api_base="https://openrouter.ai/api/v1"
)

parser = StrOutputParser()


def format_docs(docs: List[Document]) -> str:
    """
    Formats a list of Document objects into a single string for prompt input.
    """
    return "\n\n".join(doc.page_content for doc in docs)


def process_video(url: str):
    transcript = get_transcript(url)
    chunks = split_transcript(transcript)
    embedder = get_embedder()
    vector_store = build_vector_store(chunks, embedder)
    return vector_store


def build_rag_chain(vector_store):
    retriever = get_retriever(vector_store)

    test_docs = retriever.invoke("test")
    print(f"[DEBUG] Retriever returned {len(test_docs)} docs")
    
    prompt = get_rag_prompt()


    parallel_chain = RunnableParallel({
        "context": retriever | RunnableLambda(format_docs),
        "input": RunnablePassthrough()
    })

    Rag_chain = parallel_chain | prompt | llm | parser

    return Rag_chain


def ask_question(rag_chain, question: str) -> str:
    """
    Executes the RAG chain with the given question and returns the answer.
    """
    return rag_chain.invoke(question)


