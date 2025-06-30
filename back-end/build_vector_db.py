import os
from langchain_community.document_loaders import PyPDFLoader, TextLoader, UnstructuredWordDocumentLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEmbeddings
from typing import Union


loader: Union[PyPDFLoader, TextLoader, UnstructuredWordDocumentLoader]

data_dir = "data"

all_docs = []

for filename in os.listdir(data_dir):
    filepath = os.path.join(data_dir, filename)

    if filename.endswith(".pdf"):
        loader = PyPDFLoader(filepath)
    elif filename.endswith(".md") or filename.endswith(".txt"):
        loader = TextLoader(filepath, encoding='utf-8')
    elif filename.endswith(".docx"):
        loader = UnstructuredWordDocumentLoader(filepath)
    else:
        continue

    docs = loader.load()
    for doc in docs:
        doc.metadata["source"] = filename
    all_docs.extend(docs)

splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
chunks = splitter.split_documents(all_docs)


embedding = HuggingFaceEmbeddings(
    model_name="all-MiniLM-L6-v2",
    model_kwargs={"device": "cpu"}
)

db = FAISS.from_documents(chunks, embedding)
db.save_local("db_faiss")