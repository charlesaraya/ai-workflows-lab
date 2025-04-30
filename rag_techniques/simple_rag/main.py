# main.py
from pipeline import run_pipeline
from config import load_config

if __name__ == "__main__":
    config = load_config("config/config.yaml")
    raq_chain = run_pipeline(config)

    print("\nAsk me anything about our customer data (type 'exit' to quit)\n")
    while True:
        query = input(">> ")
        if query.lower() in ["exit", "quit"]:
            print("Exiting...")
            break
        try:
            response = raq_chain.invoke({"input": query})
            print(f"\n{response['answer']}\n")
        except Exception as e:
            print(f"Error: {e}")