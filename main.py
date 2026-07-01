from langchain_core.messages import HumanMessage
from src.core.nodes import generate_query_or_respond

def main():
   state = {"messages": [HumanMessage(content="Cześć, jak się masz?")]}
   result = generate_query_or_respond(state)
   print(result["messages"][-1].content)

if __name__ == "__main__":
   main()
