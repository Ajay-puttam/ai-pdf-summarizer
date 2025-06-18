# 📄 AI PDF Summarizer

An AI-powered PDF summarization tool built using Python, Streamlit, and Hugging Face Transformers.

This app allows users to upload PDF files and generate concise summaries using state-of-the-art NLP models. It now includes a chatbot feature to interactively ask questions based on the PDF content.

---

## 🚀 Features

- 📤 Upload any PDF document
- 🧠 Summarize long PDFs using `distilBART` from Hugging Face
- 📄 View full extracted text
- 📥 Download the AI-generated summary as a `.txt` file
- 💬 **NEW**: Chat with your PDF via an integrated external chatbot

---

## 💬 Chatbot Integration

After summarizing your PDF, you can now interact with the document using a chatbot to ask specific questions.

👉 [Click here to open the PDF Chatbot](https://chatwithpdf-ebtfg4y3yfjyhphqvsxcdc.streamlit.app/)

> Upload the same PDF to the chatbot and get context-aware answers.

---

## 🛠️ Tech Stack

- Python 3.11+
- Streamlit
- Hugging Face Transformers (`sshleifer/distilbart-cnn-12-6`)
- PyPDF2

---

## 🧪 How to Run Locally

1. **Clone the repository**
   ```bash
   git clone https://github.com/Ajay-puttam/ai-pdf-summarizer.git
   cd ai-pdf-summarizer
   pip install -r requirements.txt
   streamlit run ai_pdf_summarizer.py
