from typing import Literal

from langchain_core.messages import HumanMessage
from langgraph.graph import MessagesState

from core.models import grader_model, response_model
from core.prompts import GENERATE_PROMPT
from core.validation import GradeDocuments


def generate_query_or_respond(state: MessagesState):
    """LLM decyduje: wywołać tool search_sages_trainings (RAG) albo odpowiedzieć od razu."""
    response = response_model.invoke(state["messages"])
    if response.tool_calls:
        print(f"  [workflow] → retrieve: {response.tool_calls[0]['args']}")
    else:
        print(f"  [workflow] → odpowiedź bezpośrednia: {response.content[:120]}")
    return {"messages": [response]}