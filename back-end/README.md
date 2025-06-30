# 🔍 Document Search Engine – Back-End

This is the back-end of a **Proof of Concept (PoC)** for an internal document search engine.  
It is built with **Python** and **FastAPI**, and exposes a **RESTful API** to perform semantic search on embedded documents using **FAISS**.


## 🚀 Features

- 🧠 Semantic search using text embeddings
- ⚡ Fast and lightweight API with FastAPI
- 🗂️ Vector store powered by FAISS
- 🧪 Ready for local development and prototyping
- 📄 Host original documents to provide additional context for search results

## 📦 Installation

Clone the repository and install the required dependencies:

```bash
pip install -r requirements.txt
```
*Note : Make sure you have Python 3.8+ installed.*

## 🏗️ Build the Vector Database

To prepare your search engine, you first need to build the FAISS vector index from your document corpus:
    
```bash
python build_vector_db.py
```
This script parses and embeds documents (PDFs, Word files, etc.) and saves them to a FAISS index for later querying.

The current dataset is based on the document reclaiming-climate-justice.pdf (https://www.amnesty.org/en/documents/ior40/9530/2025/en/). The two others documents have been generated with MistralAI.

## 🏃 Run the API Server

To start the FastAPI server, run:

```bash
uvicorn main:app --reload
```
This will start the server on `http://localhost:8000` with live reloading enabled.
The API documentation will be available at `http://localhost:8000/docs`.