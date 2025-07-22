# 📄 RAG System: Insurance Document Q&A

A **Retriever-Augmented Generation (RAG)** system enabling intelligent Q&A over PDF insurance documents. This project integrates:

- OCR for text extraction
- Embeddings & vector search
- LLM-powered question answering
- A Streamlit frontend
- A FastAPI backend API
- Dockerized for deployment

---

## 📁 Project Structure

.
├── api/ # FastAPI backend
│ └── api.py
│
├── app/ # Streamlit frontend
│ └── streamlit_app.py
│
├── chatbot/ # Chatbot and QA logic
│ └── chatbot.py
│
├── embeddings/ # Embeddings utility functions
│ └── embed_text.py
│
├── ocr/ # OCR utilities
│ └── ocr_extractor.py
│
├── vectorstore/ # Vector store files (auto-generated)
│ ├── faiss.index
│ └── chunks.pkl
│
├── data/ # Uploaded PDFs
│
├── main.py # Pipeline to process PDFs and generate embeddings
├── requirements.txt # Python dependencies
├── Dockerfile # Docker configuration
├── docker-compose.yml # Docker Compose configuration
├── Makefile # Automation scripts
├── .env # Environment variables (API keys)
└── README.md



## 🚀 Quickstart

### ✅ Prerequisites

- Python 3.9+
- Tesseract OCR & Poppler:
  ```bash
  sudo apt update
  sudo apt install tesseract-ocr poppler-utils
Docker (optional but recommended)

🛠️ Installation (without Docker)
Clone the repository:


git clone <repo-url>
cd <repo-directory>
Setup virtual environment and install dependencies:


make venv
make install
Add your OpenAI key in a .env file:


OPENAI_API_KEY=your_openai_key
Run:

make run-api    # Start FastAPI backend
make run-app    # Start Streamlit frontend
🐳 Docker Deployment
✅ Build and Run


make build-docker
make run-docker
Or directly:

docker-compose up
Access
Streamlit App: http://localhost:8501

FastAPI Backend: http://localhost:8000

🧩 API Endpoints
Endpoint	Method	Description
/upload/	POST	Upload & process a PDF
/ask/	POST	Query the document

🖥️ Makefile Commands
Command	Description
make venv	Create virtual environment
make install	Install dependencies
make run-api	Start FastAPI backend
make run-app	Start Streamlit app
make build-docker	Build Docker image
make run-docker	Run Docker container
make clean	Clean generated vector files

✅ Responsibilities by Module
Folder/File	Responsibility
ocr/	OCR processing utilities
embeddings/	Embedding generation utilities
vectorstore/	Vector store: FAISS & chunks.pkl
chatbot/	Chatbot question answering logic
api/	FastAPI backend
app/	Streamlit frontend

🎨 Features
Upload PDF and auto-process with embeddings

Ask contextual questions about uploaded documents

Frontend-backend separation via API

Supports both API and UI interaction

Dockerized for easy deployment

🔮 Future Enhancements
Add chat history / memory

Multi-document support

Authentication / User sessions

Cloud hosting guidelines

🤝 Contributing
Contributions are welcome! Feel free to open issues or submit pull requests.

📜 License
MIT License

