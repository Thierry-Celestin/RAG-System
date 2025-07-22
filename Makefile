.PHONY: venv install install-openai install-langchain-community install-poppler install-tesseract run-pipeline run-app run-api build-docker run-docker clean

venv:
	@test -d ocr-env || python3 -m venv ocr-env

install: venv
	. ocr-env/bin/activate && pip install --upgrade pip && pip install -r requirements.txt
	@echo "✅ Environment set up and dependencies installed."

install-poppler:
	sudo apt update && sudo apt install -y poppler-utils
	@echo "✅ Poppler utilities installed."

install-tesseract:
	sudo apt update && sudo apt install -y tesseract-ocr
	@echo "✅ Tesseract OCR installed."

install-openai:
	. ocr-env/bin/activate && pip install openai langchain-openai
	@echo "✅ OpenAI and LangChain OpenAI installed."

install-langchain-community:
	. ocr-env/bin/activate && pip install langchain-community
	@echo "✅ LangChain Community installed."

run-pipeline:
	. ocr-env/bin/activate && python main.py

run-app:
	. ocr-env/bin/activate && streamlit run app/streamlit_app.py

run-api:
	. ocr-env/bin/activate && uvicorn api.api:app --host 0.0.0.0 --port 8000 --reload

build-docker:
	docker-compose build
	@echo "🐳 Docker images built."

run-docker:
	docker-compose up
	@echo "🚀 Running Docker Compose."

clean:
	@rm -f vectorstore/faiss.index vectorstore/chunks.pkl
	@echo "🧹 Cleaned vectorstore files."
