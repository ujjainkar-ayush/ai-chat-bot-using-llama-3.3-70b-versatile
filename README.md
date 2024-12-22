# Llama-3.3-70B Agent

This project demonstrates how to create an AI-powered chatbot using the **Llama-3.3-70B** model with the **Phi Agent** and **Groq API**. The chatbot continuously processes user queries and provides responses until the user decides to exit.

## Features
- Interactive chatbot interface.
- Utilizes the Llama-3.3-70B model for generating responses.
- Supports environment variables using **dotenv** for secure API key handling.

## Prerequisites
- Python 3.11 or higher.
- Groq API access and credentials.

## Installation

1. **Clone the repository:**
   ```bash
   git clone <repository-url>
   cd <repository-name>
   ```

2. **Create a virtual environment:**
   ```bash
   python -m venv env
   source env/bin/activate  # Linux/Mac
   .\env\Scripts\activate  # Windows
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables:**
   - Create a `.env` file in the project directory.
   - Add the required keys, such as:
     ```plaintext
     GROQ_API_KEY=your_api_key_here
     ```

## Usage

1. **Run the chatbot:**
   ```bash
   python main.py
   ```

2. **Interact with the chatbot:**
   - Type a question or message.
   - Type `exit` to quit the chatbot.

## Code Overview

```python
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
```

## Dependencies
- **Phi Agent**
- **Groq API**
- **dotenv**

## License
This project is licensed under the MIT License.

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## Contact
For questions or support, feel free to open an issue on GitHub.

