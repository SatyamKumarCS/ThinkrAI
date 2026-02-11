import os
import google.generativeai as genai
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_chroma import Chroma
from backend.guardrails.prompt import SOCRATIC_SYSTEM_PROMPT
from dotenv import load_dotenv

load_dotenv()

class SocraticEngine:
    def __init__(self):
        #Initialise Gemini
        genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
        self.model=genai.GenerativeModel('gemini-1.5-flash')
        #Initialise ChromeDB
        self.embedding=HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
        self.vector_db=Chroma(
            persist_directory="data/chroma_db",
            embedding_function=self.embedding
        )

    def query(self,user_input:str):
        docs=self.vector_db.similarity_search(user_input,k=3)
        context_text='\n\n'.join([doc.page_content for doc in docs])
        full_prompt=SOCRATIC_SYSTEM_PROMPT.format(context=context_text,query=user_input)
        response=self.model.generate_content(full_prompt)

        return response.text