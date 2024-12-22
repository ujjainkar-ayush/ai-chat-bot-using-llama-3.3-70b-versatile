from phi.agent import Agent
from phi.model.groq import Groq
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Initialize the agent with the Groq model
agent = Agent(
    model=Groq(id="llama-3.3-70b-versatile")
)

def main():
    # Run continuously until the user decides to exit
    while True:
        # Get input from the user
        instruction = input("Message llama (or type 'exit' to quit): ")
        
        if instruction.lower() == 'exit':
            print("Exiting the program...")
            break  # Exit the loop if user types 'exit'
        
        # Pass the instruction to the agent inside the f-string
        agent.print_response(f"Give the answer of the question {instruction} as the user want")

if __name__ == "__main__":
    main()
