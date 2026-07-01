from langchain_core.tools import create_retriever_tool

from core.hybrid_retriever import get_hybrid_retriever

retriever = get_hybrid_retriever()
retriever_tool = create_retriever_tool(
    retriever,
    "search_sages_trainings",
    "Wyszukuje szkolenia Sages — zwraca opisy, kategorie, czas trwania i linki do programów.",
)
