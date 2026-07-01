from langchain_core.messages import HumanMessage
from src.core.graph import graph

def main():
   state = {"messages": [HumanMessage(content="Szanowna Pani, Ile to jest 2 + 2?")]}
   result = graph.invoke(state)
   print(result["messages"][-1].content)

if __name__ == "__main__":
   main()
