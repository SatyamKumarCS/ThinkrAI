# 🧠 ThinkrAI: The Socratic DSA Tutor

> **Master Data Structures & Algorithms through guided inquiry, not memorization.**

![ThinkrAI Banner](https://via.placeholder.com/1200x400?text=ThinkrAI+%7C+Socratic+Tutor+System)  
*(Add a screenshot of your beautiful dark-mode UI here)*

## 🚀 Overview
**ThinkrAI** is an advanced AI-powered tutoring system designed to teach **Data Structures and Algorithms (DSA)** using the **Socratic Method**. Instead of providing direct answers or code snippets, ThinkrAI acts as a personalized mentor, asking probing questions to guide students toward the solution. This approach fosters deep understanding and critical thinking skills essential for technical interviews and software engineering.

Built with a local-first architecture, ThinkrAI leverages **Ollama (Gemma 3: 1B)** for privacy-focused, latency-free interactions, and **RAG (Retrieval-Augmented Generation)** to ground responses in verified educational content.

## ✨ Key Features
-   **Socratic Guidance Engine**: A custom-engineered system prompt ensures the AI never gives the answer directly but leads the user to it step-by-step.
-   **RAG-Powered Knowledge Base**: Ingests textbooks and technical documentation (PDFs) to provide accurate, context-aware responses.
-   **Local LLM Integration**: Runs entirely offline using **Ollama** and the **Gemma 3** model, ensuring data privacy and zero API costs.
-   **Modern Dark UI**: A sleek, dark-themed interface built with **Streamlit** and custom CSS, featuring glassmorphism and animated elements.
-   **Semantic Search**: Utilizes **ChromaDB** and **HuggingFace Embeddings** for precise context retrieval.
-   **Memory & Context**: Maintains chat history to support multi-turn conversations and deep dives into complex topics.

## 🛠️ Tech Stack
-   **Frontend**: Streamlit (Python), Custom CSS3
-   **LLM Backend**: Ollama, LangChain
-   **Vector Database**: ChromaDB
-   **Embeddings**: HuggingFace (`all-MiniLM-L6-v2`)
-   **Language**: Python 3.10+

## 🏗️ Architecture
1.  **Ingestion**: Educational PDFs are loaded, split into chunks, and embedded using HuggingFace models.
2.  **Storage**: Embeddings are stored in a local ChromaDB vector store.
3.  **Retrieval**: User queries trigger a similarity search to fetch relevant context.
4.  **Generation**: The context and query are passed to the **Gemma 3** model via a strict usage prompt that enforces Socratic dialogue rules.
5.  **Interface**: The response is streamed to the Streamlit frontend in real-time.

## 🚀 Getting Started

### Prerequisites
-   Python 3.10 or higher
-   [Ollama](https://ollama.com/) installed and running

### Installation

1.  **Clone the Repository**
    ```bash
    git clone https://github.com/SatyamKumarCS/ThinkrAI.git
    cd ThinkrAI
    ```

2.  **Create a Virtual Environment**
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    ```

3.  **Install Dependencies**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Setup Ollama**
    Ensure Ollama is running and pull the Gemma 3 model:
    ```bash
    ollama pull gemma3:1b
    ```

5.  **Ingest Knowledge Base**
    Place your DSA textbook (PDF) in `data/raw/` and run:
    ```bash
    python backend/scripts/ingest.py
    ```

6.  **Run the Application**
    ```bash
    streamlit run frontend/app.py
    ```

## 📸 Screenshots
| Chat Interface | Socratic Dialogue |
|:---:|:---:|
| *(Add Screenshot)* | *(Add Screenshot)* |

## 🤝 Contributing
Contributions are welcome! Please feel free to submit a Pull Request.

## 📄 License
This project is licensed under the MIT License.

---
**Author**: Satyam Kumar
