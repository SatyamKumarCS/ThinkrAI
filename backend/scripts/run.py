import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))

from backend.app.engine import SocraticEngine

def main():
    try:
        engine = SocraticEngine()
        print("Socratic Engine initialized successfully.")
        
        while True:
            query = input("\nEnter your question (or 'quit' to exit): ")
            if query.lower() in ('quit', 'exit'):
                break
            
            print("\nThinking...")
            response = engine.query(query)
            print(f"\nResponse:\n{response}")
            
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
