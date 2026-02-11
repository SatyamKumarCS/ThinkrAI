import os
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_chroma import Chroma

def run_ingest():
    raw_path='data/raw'
    persist_path='data/chroma_db/'

    print("Reading PDFs from data/raw/ :: ")
    docs=[]
    if not os.path.exists(raw_path):
        os.makedirs(raw_path)

    for file in os.listdir(raw_path):
        if file.endswith('.pdf'):
            loader=PyPDFLoader(os.path.join(raw_path,file))
            docs.extend(loader.load())

    if not docs:
        print("Error: No PDFs found in data/raw/. Please add a PDF and try again.")
        return

    text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=100)
    chunks = text_splitter.split_documents(docs)

    print("Generating embeddings...")
    embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")

    vector_db = Chroma.from_documents(
        documents=chunks,
        embedding=embeddings,
        persist_directory=persist_path
    )
    
    print(f"Success! {len(chunks)} chunks stored in {persist_path}")

if __name__ == "__main__":
    run_ingest()