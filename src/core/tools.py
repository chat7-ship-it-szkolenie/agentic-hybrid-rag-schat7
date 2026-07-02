from langchain_core.prompts import PromptTemplate
from langchain_core.tools import create_retriever_tool

from core.hybrid_retriever import get_hybrid_retriever

DOCUMENT_PROMPT = PromptTemplate.from_template(
    "{page_content}\nLink do programu szkolenia: {pdf_url}"
)


retriever = get_hybrid_retriever()
retriever_tool = create_retriever_tool(
    retriever,
    "search_sages_trainings",
    "Wyszukuje szkolenia Sages — zwraca opisy, kategorie, czas trwania i linki do programów.",
    document_prompt=DOCUMENT_PROMPT
)
