from langchain_core.messages import HumanMessage
from src.core.graph import graph

def main():
   state = {"messages": [HumanMessage(content="Jakie szkolenia Sages są dostępne w kategorii 'Data Science' i ile trwają?")]}
   result = graph.invoke(state)
   print(result["messages"][-1].content)

if __name__ == "__main__":
   main()
