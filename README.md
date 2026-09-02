# LangChain Tutorial

A beginner-friendly, hands-on tutorial covering the fundamentals of **LangChain** and how to build applications powered by Large Language Models (LLMs).

This repository starts from environment setup and gradually covers LangChain's core concepts, components, and practical examples.

---

## 🚀 Getting Started

### 1. Install `uv`

`uv` is a fast Python package and project manager written in Rust.

If you don't already have `uv`, install it using:

**macOS / Linux**

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

**Windows**

```powershell
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```

Verify the installation:

```bash
uv --version
```

---

### 2. Create a New Python Environment

Navigate to the project directory:

```bash
cd langchain-tutorial
```

Create a virtual environment:

```bash
uv venv
```

This creates a `.venv` directory in your project.

---

### 3. Activate the Environment

**macOS / Linux**

```bash
source .venv/bin/activate
```

**Windows CMD**

```cmd
.venv\Scripts\activate
```

**Windows PowerShell**

```powershell
.venv\Scripts\Activate.ps1
```

You should now see something similar to:

```text
(.venv) $
```

---

### 4. Install Dependencies

Install LangChain:

```bash
uv pip install langchain
```

For OpenAI models:

```bash
uv pip install langchain-openai
```

For commonly used LangChain integrations:

```bash
uv pip install langchain-community
```

You can install everything together:

```bash
uv pip install langchain langchain-openai langchain-community
```

---

### 5. Create `requirements.txt`

If you want to export the installed dependencies:

```bash
uv pip freeze > requirements.txt
```

To install them later:

```bash
uv add "dependency_name"

uv pip install -r requirements.txt
```

---

## 🔐 API Keys

Many LangChain examples require an API key.

Create a `.env` file:

```text
OPENAI_API_KEY=your_api_key_here
```

Install `python-dotenv`:

```bash
uv pip install python-dotenv
```

Load the environment variables:

```python
from dotenv import load_dotenv

load_dotenv()
```

### ⚠️ Important

Never commit your API keys to GitHub.

Add `.env` to `.gitignore`:

```text
.env
.venv/
__pycache__/
*.pyc
```

---

# 📚 What This Tutorial Covers

## Introduction to LangChain

* What is LangChain?
* Why LangChain?
* LLM application architecture
* LangChain ecosystem
* Models
* Prompts
* Chains
* Retrievers
* Tools
* Agents
* Memory
* Document processing
* Streaming

---

---

# 🧠 Key Concepts to Master

Before moving to advanced Agentic AI development, make sure you understand:

* LLMs
* Chat models
* Prompt engineering
* Prompt templates
* LCEL
* Chains
* Structured output
* Function/tool calling
* Embeddings
* Vector databases
* Similarity search
* Retrievers
* RAG
* Agents
* Memory/state
* Streaming
* LangGraph

---

# 📌 Goal of This Repository

The goal of this tutorial is to move from:

```text
Beginner
   ↓
LangChain Fundamentals
```

The emphasis is on **understanding the concepts by building practical examples**, rather than simply memorizing APIs.

---

## ⭐ If You Find This Useful

If this repository helps you learn LangChain:

* ⭐ Star the repository
* 🍴 Fork it
* 📚 Follow the tutorials
* 🛠️ Build your own projects
* 🚀 Experiment with different LLMs and tools

---

## 📄 License

This project is intended for educational and learning purposes.
