import faiss
import numpy as np
import pickle

def build_faiss_index(embeddings):
    dim = len(embeddings[0])
    index = faiss.IndexFlatL2(dim)
    index.add(np.array(embeddings).astype('float32'))
    return index

def save_index(index, filename="vectorstore/faiss.index"):
    faiss.write_index(index, filename)

def save_chunks(chunks, filename="vectorstore/chunks.pkl"):
    with open(filename, 'wb') as f:
        pickle.dump(chunks, f)
