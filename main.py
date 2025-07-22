import sys
from ocr.ocr_extractor import extract_text_from_pdf
from preprocessing.clean_text import clean_text
from embeddings.embed_text import generate_embeddings
from vectorstore.store_vectors import build_faiss_index, save_index, save_chunks

def run_pipeline(pdf_path: str, verbose: bool = True):
    """Full processing pipeline: OCR, clean text, generate embeddings, save vector index and chunks."""
    if verbose:
        print(f"🚀 Starting pipeline for PDF: {pdf_path}")

    raw_text = extract_text_from_pdf(pdf_path)
    if verbose:
        print("✅ OCR extraction completed.")

    cleaned_text = clean_text(raw_text)
    if verbose:
        print("✅ Text cleaning completed.")

    chunks, embeddings = generate_embeddings(cleaned_text)
    if verbose:
        print(f"✅ Generated {len(chunks)} text chunks and embeddings.")

    index = build_faiss_index(embeddings)
    save_index(index)
    save_chunks(chunks)

    if verbose:
        print("🎉 Pipeline completed. Vector store is ready.")

    return True  # You can also return the number of chunks or index info if useful

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python main.py <path_to_pdf>")
        sys.exit(1)

    pdf_path = sys.argv[1]
    run_pipeline(pdf_path)
