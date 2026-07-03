from langchain_openai import ChatOpenAI

from config import settings

response_model = ChatOpenAI(
    model="gpt-4o",
    temperature=0.0,
    api_key=settings.openai_api_key,
)
grader_model = ChatOpenAI(
    model="gpt-4o",
    temperature=0.0,
    api_key=settings.openai_api_key,
)
