# LangGraph & Chainlit Examples

This repository demonstrates how to integrate **LangGraph** with **Chainlit** for building interactive applications powered by LLMs (Large Language Models).

## 🛠️ Environment Setup

### Step 1: Create a Virtual Environment

It's recommended to use a virtual environment to keep your dependencies isolated.

```bash
conda create --prefix ./.venv -n chainlit python=3.11
conda activate /home/yizaochen/codes/langgraph_tutorial/.venv
```

### Step 2: Install Dependencies

Install all necessary packages with a single command:

```bash
pip install -U langgraph langsmith langchain-openai python-dotenv tavily-python langchain_community chainlit langchain
```

> **Note**: Keeping your packages up to date ensures you have the latest features and bug fixes.

## 🚀 Running the Chatbot Examples

This repository includes several Chainlit chatbot examples. Follow the steps below to run each example:

### 1. Simple Chatbot Example

Path: `./chainlit_examples/simple_chat/app.py`

This is a simple chatbot that uses **Chainlit** as the UI and **LangGraph** as the backend. It has streaming capabilities for real-time interaction.

To run the simple chatbot:

```bash
cd ./examples/chainlit_examples/simple_chat
chainlit run app.py -w
```

- The `-w` flag enables **watch mode**, allowing the server to automatically restart upon code changes.

### 2. [Future Examples]

This section is reserved for future chatbot examples. As more examples are added, they will be documented here with specific instructions.

## 📚 Reference Materials

Here are some resources to help you get started:

- [Chainlit Documentation: Integrating with LangChain](https://docs.chainlit.io/integrations/langchain)
- [LangGraph Documentation](https://langchain-ai.github.io/langgraph/tutorials/)
- [chainlit_langgraph](https://github.com/brucechou1983/chainlit_langgraph)
