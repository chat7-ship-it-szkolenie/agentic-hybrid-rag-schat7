"""Hybrydowy retriever: gęsty (Chroma/embeddings) + rzadki (BM25), łączone przez EnsembleRetriever.

Korpus BM25 budowany jest z tych samych chunków, które są już zaindeksowane
w Chroma (vs.get()), więc oba retrievery zawsze widzą identyczny zbiór dokumentów.
"""
import os

from langchain_chroma import Chroma
from langchain_classic.retrievers import EnsembleRetriever
from langchain_community.retrievers import BM25Retriever
from langchain_core.documents import Document
from langchain_openai import OpenAIEmbeddings

from config import settings
from core.retriever import CHROMA_DIR, COLLECTION_NAME


def _load_indexed_documents() -> tuple[Chroma, list[Document]]:
    if not os.path.isdir(CHROMA_DIR) or not os.listdir(CHROMA_DIR):
        raise RuntimeError(
            f"Indeks Chroma nie istnieje: {CHROMA_DIR}\n"
            "Uruchom najpierw: python scripts/build_index.py"
        )
    embeddings = OpenAIEmbeddings(model="text-embedding-3-small", api_key=settings.openai_api_key)
    vs = Chroma(
        collection_name=COLLECTION_NAME,
        embedding_function=embeddings,
        persist_directory=CHROMA_DIR,
    )
    stored = vs.get()
    docs = [
        Document(page_content=text, metadata=meta or {})
        for text, meta in zip(stored["documents"], stored["metadatas"])
    ]
    return vs, docs


def get_hybrid_retriever(
    k: int = 4,
    dense_weight: float = 0.5,
    bm25_weight: float = 0.5,
) -> EnsembleRetriever:
    """Zwraca retriever łączący dense (Chroma/cosine) i sparse (BM25) ranking.

    `dense_weight` / `bm25_weight` to wagi RRF-podobnego łączenia rankingów
    w EnsembleRetriever — parametr do benchmarkowania (np. 0.5/0.5, 0.7/0.3, ...).
    """
    vs, docs = _load_indexed_documents()
    if not docs:
        raise RuntimeError(f"Indeks Chroma jest pusty: {CHROMA_DIR}")

    bm25_retriever = BM25Retriever.from_documents(docs)
    bm25_retriever.k = k

    dense_retriever = vs.as_retriever(search_kwargs={"k": k})

    return EnsembleRetriever(
        retrievers=[bm25_retriever, dense_retriever],
        weights=[bm25_weight, dense_weight],
    )
