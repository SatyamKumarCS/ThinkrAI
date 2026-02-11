import os
from langchain_chroma import Chroma
from langchain_ollama import ChatOllama
from langchain_huggingface import HuggingFaceEmbeddings
from backend.guardrails.prompt import SOCRATIC_SYSTEM_PROMPT
from dotenv import load_dotenv

load_dotenv()

class SocraticEngine:
    def __init__(self):

        self.llm_provider = os.getenv("LLM_PROVIDER", "ollama").lower()
        self.model_name = os.getenv("LLM_MODEL", "gemma3:1b")
        
        if self.llm_provider == "openrouter":
            from langchain_openai import ChatOpenAI
            api_key = os.getenv("OPENROUTER_API_KEY")
            if not api_key:
                raise ValueError("OPENROUTER_API_KEY is required for OpenRouter provider")
                
            self.model = ChatOpenAI(
                base_url="https://openrouter.ai/api/v1",
                api_key=api_key,
                model=self.model_name
            )
            print(f"Connected to OpenRouter with model: {self.model_name}")
        elif self.llm_provider == "groq":
            from langchain_groq import ChatGroq
            api_key = os.getenv("GROQ_API_KEY")
            if not api_key:
                raise ValueError("GROQ_API_KEY is required for Groq provider")
            
            self.model = ChatGroq(
                groq_api_key=api_key,
                model_name=self.model_name
            )
            print(f"Connected to Groq with model: {self.model_name}")
        else:
            self.model = ChatOllama(model=self.model_name)
            print(f"Connected to Local Ollama with model: {self.model_name}")

        self.embedding = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
        self.vector_db = Chroma(
            persist_directory="data/chroma_db",
            embedding_function=self.embedding
        )

    def query(self,user_input:str):
        docs=self.vector_db.similarity_search(user_input,k=3)
        context_text='\n\n'.join([doc.page_content for doc in docs])
        full_prompt=SOCRATIC_SYSTEM_PROMPT.format(context=context_text,query=user_input)
        response=self.model.invoke(full_prompt)

        return response.content