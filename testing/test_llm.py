from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
import os

load_dotenv()

# model = ChatOpenAI(model='gpt-4o')
model = ChatOpenAI(
    model="openai/gpt-4o-mini",   
    openai_api_key=os.getenv("OPENROUTER_API_KEY"),
    openai_api_base="https://openrouter.ai/api/v1",
    temperature=0.8
)

result = model.invoke("suggest me five Indian male name?")

print(result.content)