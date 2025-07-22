import faiss
import pickle
import numpy as np
from sentence_transformers import SentenceTransformer
from langchain_openai import ChatOpenAI  # updated import based on LangChain deprecation
from langchain.prompts import PromptTemplate
from langchain.schema import HumanMessage
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
if not OPENAI_API_KEY:
    raise ValueError("OPENAI_API_KEY not found. Please set it in your .env file.")

# Paths to your saved vector index and chunks
INDEX_PATH = "vectorstore/faiss.index"
CHUNKS_PATH = "vectorstore/chunks.pkl"

# Global variables to hold index and chunks
index = None
chunks = None

# Initialize embedding model and language model
embedder = SentenceTransformer('all-MiniLM-L6-v2')
llm = ChatOpenAI(api_key=OPENAI_API_KEY, model="gpt-4")  # updated import usage

def load_index_and_chunks():
    """Load the FAISS index and chunks from disk into global variables."""
    global index, chunks
    if os.path.exists(INDEX_PATH) and os.path.exists(CHUNKS_PATH):
        index = faiss.read_index(INDEX_PATH)
        with open(CHUNKS_PATH, "rb") as f:
            chunks = pickle.load(f)
        print("✅ Loaded FAISS index and chunks successfully.")
    else:
        raise FileNotFoundError("FAISS index or chunks not found. Run the pipeline first.")

def search_similar_chunks(query, k=3):
    """Return the top-k most relevant text chunks for a query."""
    if index is None or chunks is None:
        raise ValueError("Index and chunks not loaded. Please run load_index_and_chunks() first.")

    query_embedding = embedder.encode([query])
    D, I = index.search(np.array(query_embedding).astype('float32'), k)
    return [chunks[i] for i in I[0]]

def answer_question(query):
    """Answer a user question based on the loaded document context."""
    relevant_chunks = search_similar_chunks(query)
    context = " ".join(relevant_chunks)

    prompt_template = PromptTemplate(
        input_variables=["context", "question"],
        template="""
You are an insurance document assistant.

Context: {context}

Question: {question}

Provide a clear, comprehensive, and professional answer based on the context provided.
"""
    )
    prompt = prompt_template.format(context=context, question=query)

    # Use .invoke() instead of __call__ to avoid deprecation warning
    response = llm.invoke([HumanMessage(content=prompt)])
    return response.content

if __name__ == "__main__":
    try:
        load_index_and_chunks()
        question = "What is my deductible?"
        print("Q:", question)
        print("A:", answer_question(question))
    except Exception as e:
        print(f"Error: {e}")
