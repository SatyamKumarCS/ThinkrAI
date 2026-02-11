# 🧠 ThinkrAI: The Socratic DSA Tutor

> **Master Data Structures & Algorithms through guided inquiry, not memorization.**

![ThinkrAI Banner](https://via.placeholder.com/1200x400?text=ThinkrAI+%7C+DSA+Socratic+Tutor)  
*(Add a screenshot of your beautiful dark-mode UI here)*

## 🚀 Overview
**ThinkrAI** is an advanced AI-powered tutoring system designed to teach **Data Structures and Algorithms (DSA)** using the **Socratic Method**. Instead of providing direct answers or code snippets, ThinkrAI acts as a personalized mentor, asking probing questions to guide students toward the solution. This approach fosters deep understanding and critical thinking skills essential for technical interviews and software engineering.

Built with a **Hybrid Architecture**:
*   **Local Development**: Uses **Ollama (Gemma 3: 1B)** for privacy-focused, offline interactions.
*   **Cloud Deployment**: Automatically switches to **Groq (Llama 3)** for high-speed, scalable inference on platforms like Render or Streamlit Cloud.

## ✨ Key Features
-   **Socratic Guidance Engine**: A custom-engineered system prompt ensures the AI never gives the answer directly but leads the user to it step-by-step.
-   **RAG-Powered Knowledge Base**: Ingests textbooks and technical documentation (PDFs) to provide accurate, context-aware responses.
-   **Hybrid LLM Support**: Seamlessly switches between local Ollama and cloud-based Groq based on environment variables.
-   **Modern Dark UI**: A sleek, dark-themed interface built with **Streamlit** and custom CSS, featuring glassmorphism and animated elements.
-   **Semantic Search**: Utilizes **ChromaDB** and **HuggingFace Embeddings** for precise context retrieval.

## 🛠️ Tech Stack
-   **Frontend**: Streamlit (Python), Custom CSS3
-   **LLM Providers**: 
    -   **Ollama**: Local execution (Gemma 3)
    -   **Groq**: Cloud inference (Llama 3.3)
-   **Orchestration**: LangChain
-   **Vector Database**: ChromaDB
-   **Embeddings**: HuggingFace (`all-MiniLM-L6-v2`)
-   **Language**: Python 3.10+

## 🏗️ Architecture
1.  **Ingestion**: Educational PDFs are loaded, split into chunks, and embedded using HuggingFace models.
2.  **Storage**: Embeddings are stored in a local ChromaDB vector store.
3.  **Retrieval**: User queries trigger a similarity search to fetch relevant context.
4.  **Generation**: The context and query are passed to the selected LLM (Ollama or Groq).
5.  **Interface**: The response is streamed to the Streamlit frontend in real-time.

## 🚀 Getting Started

### Prerequisites
-   Python 3.10 or higher
-   [Ollama](https://ollama.com/) installed (for local mode)
-   [Groq API Key](https://console.groq.com/) (for cloud mode)

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

4.  **Setup Environment (`.env`)**
    Create a `.env` file in the root directory:
    ```env
    # Optional: For Cloud Mode (Groq)
    GROQ_API_KEY=your_groq_api_key_here
    ```

### Running Locally (Ollama Mode)
1.  Ensure Ollama is running and pull the model:
    ```bash
    ollama pull gemma3:1b
    ```
2.  Run the application:
    ```bash
    streamlit run frontend/app.py
    ```
    *(By default, if `LLM_PROVIDER` is not set, it uses Ollama).*

<<<<<<< Updated upstream
## 📸 Screenshots
![ThinkrAI UI](screenshot/ui.png)
=======
### Running in Cloud Mode (Groq)
To use Groq (e.g., for deployment or faster inference), set the environment variable:
```bash
export LLM_PROVIDER="groq"
export LLM_MODEL="llama-3.3-70b-versatile"
streamlit run frontend/app.py
```

## ☁️ Deployment (Render / Streamlit Cloud)
To deploy this app for free:
1.  Push your code to GitHub.
2.  Connect your repository to **Render** or **Streamlit Cloud**.
3.  **Critical**: Set the following Environment Variables in the cloud dashboard:
    *   `LLM_PROVIDER`: `groq`
    *   `GROQ_API_KEY`: `(Your Groq API Key)`
    *   `LLM_MODEL`: `llama-3.3-70b-versatile`

>>>>>>> Stashed changes
## 🤝 Contributing
Contributions are welcome! Please feel free to submit a Pull Request.

## 📄 License
This project is licensed under the MIT License.

---
**Author**: Satyam Kumar
