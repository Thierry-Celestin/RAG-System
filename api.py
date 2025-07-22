from fastapi import FastAPI, UploadFile, File, HTTPException
from chatbot.chatbot import answer_question
from main import run_pipeline
import shutil
import os

app = FastAPI()

UPLOAD_FOLDER = 'data/'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.post("/upload/")
async def upload_document(file: UploadFile = File(...)):
    if not file.filename.endswith('.pdf'):
        raise HTTPException(status_code=400, detail="Only PDF files are allowed.")

    file_path = os.path.join(UPLOAD_FOLDER, file.filename)
    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    run_pipeline(file_path)
    return {"message": f"Successfully processed {file.filename}"}


@app.post("/ask/")
async def ask_question(question: str):
    if not os.path.exists('vectorstore/faiss.index'):
        raise HTTPException(status_code=404, detail="No vector store found. Please upload and process a document first.")

    answer = answer_question(question)
    return {"question": question, "answer": answer}
