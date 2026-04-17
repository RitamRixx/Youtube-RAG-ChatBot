from langchain_core.prompts import ChatPromptTemplate


def get_rag_prompt()->ChatPromptTemplate:
    """
    Defines and returns a ChatPromptTemplate for generating responses from retrieved chunks.
    """
    system_template = """
    you are a helpful assistant that answers questions based on the provided video transcript context
    Rules you MUST follow:
    1. Answer ONLY using the context below. Do NOT use outside knowledge.
    2. You may combine information across multiple parts of the context.
    3. If the answer is not in the context, respond exactly with: "Sorry, I don't know the answer to that question."
    4. If the answer is partially available, give the best possible answer.
    5. Keep answers clear, concise, and structured.

    Context:
    {context}
    """

    prompt = ChatPromptTemplate.from_messages([
        ("system", system_template),
        ("human", "{input}")
    ])

    return prompt