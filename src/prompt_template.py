from langchain_core.prompts import ChatPromptTemplate


def get_rag_prompt()->ChatPromptTemplate:
    """
    Defines and returns a ChatPromptTemplate for generating responses from retrieved chunks.
    """
    system_template = """
    you are a helpful assistant that answers questions strictly based on the provided video transcript context\n
    Rules you MUST follow:\n
    1. Answer ONLY using the context below. Do NOT use outside knowledge.\n
    2. If the answer is not in the context, respond exactly with: "Sorry, I don't know the answer to that question."\n
    3. Do NOT make up, guess, or infer beyond what is explicitly stated.\n
    4. Keep answers clear, concise, and structured.\n\n
    Context:\n{context}
    """

    prompt = ChatPromptTemplate.from_messages([
        ("system", system_template),
        ("human", "{input}")
    ])

    return prompt