from dotenv import load_dotenv
from langchain_groq import ChatGroq
import os


load_dotenv()

llm = ChatGroq(
    groq_api_key = os.getenv("GROQ_API_KEY")
)