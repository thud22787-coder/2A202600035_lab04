import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI   # ← Sửa ở đây

load_dotenv()

llm = ChatOpenAI(model="gpt-4o-mini")

print(llm.invoke("Xin chào?").content)