import streamlit as st
import PyPDF2
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM, pipeline
import tempfile
import os


# ---------- Load Hugging Face Model ----------
@st.cache_resource
def load_summarizer():
    tokenizer = AutoTokenizer.from_pretrained("sshleifer/distilbart-cnn-12-6")
    model = AutoModelForSeq2SeqLM.from_pretrained("sshleifer/distilbart-cnn-12-6")
    return pipeline("summarization", model=model, tokenizer=tokenizer)


summarizer = load_summarizer()


# ---------- Extract Text from PDF ----------
def extract_text_from_pdf(uploaded_file):
    reader = PyPDF2.PdfReader(uploaded_file)
    full_text = ""
    for page in reader.pages:
        full_text += page.extract_text() or ""
    return full_text


# ---------- Chunk and Summarize ----------
def summarize_text(text, chunk_size=700, overlap=100):
    words = text.split()
    chunks = []
    i = 0
    while i < len(words):
        chunk = words[i : i + chunk_size]
        chunks.append(" ".join(chunk))
        i += chunk_size - overlap

    summary = ""
    for idx, chunk in enumerate(chunks):
        st.write(f"⏳ Summarizing chunk {idx + 1} of {len(chunks)}...")
        try:
            result = summarizer(chunk, max_length=150, min_length=30, do_sample=False)
            summary += result[0]["summary_text"] + "\n\n"
        except Exception as e:
            st.warning(f"Error summarizing chunk {idx + 1}: {e}")
    return summary.strip()


# ---------- Streamlit UI ----------
st.set_page_config(page_title="AI PDF Summarizer", layout="centered")
st.title("📄 AI PDF Summarizer")
st.markdown("🔍 Summarize any PDF using Hugging Face Transformers")

pdf_file = st.file_uploader("Upload a PDF", type=["pdf"])

if pdf_file:
    with st.spinner("📚 Extracting text from PDF..."):
        text = extract_text_from_pdf(pdf_file)

    if len(text.strip()) < 100:
        st.warning("❗ Extracted text is too short to summarize.")
    else:
        with st.spinner("🧠 Summarizing using Hugging Face model..."):
            summary = summarize_text(text)

        st.subheader("📝 Summary")
        st.write(summary)

        # ----- Download Button -----
        summary_filename = pdf_file.name.replace(".pdf", "_summary.txt")
        with tempfile.NamedTemporaryFile(
            delete=False, suffix=".txt", mode="w"
        ) as tmp_file:
            tmp_file.write(summary)
            tmp_path = tmp_file.name

        with open(tmp_path, "rb") as file:
            st.download_button(
                label="📥 Download Summary as TXT",
                data=file,
                file_name=summary_filename,
                mime="text/plain",
            )

        # Optional: View Full Extracted Text
        with st.expander("📄 View Extracted PDF Text"):
            st.text_area("Raw Text", text, height=300)

st.markdown("---")
st.caption("⚙️ Powered by Streamlit & Hugging Face Transformers")
