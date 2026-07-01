from langchain_openai import ChatOpenAI
from pydantic import BaseModel, Field

class GradeDocuments(BaseModel):
    binary_score: str = Field(description="Relevance score: 'yes' jeśli istotne, 'no' jeśli nie")
