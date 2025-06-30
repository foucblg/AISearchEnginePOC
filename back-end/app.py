from fastapi import FastAPI, Query
from pydantic import BaseModel
from langchain_community.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEmbeddings
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles


app = FastAPI()



app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

embedding = HuggingFaceEmbeddings(
    model_name="all-MiniLM-L6-v2",
    model_kwargs={"device": "cpu"}
)

db = FAISS.load_local("db_faiss", embedding, allow_dangerous_deserialization=True)

class QueryRequest(BaseModel):
    query: str
    k: int = 3

@app.get("/search")
def search(query: str = Query(...), k: int = 3):
    results_with_scores = db.similarity_search_with_score(query, k)
    response_data = []
    for doc, score in results_with_scores:
        response_data.append({
            "page_content": doc.page_content,
            "metadata": doc.metadata,
            "score": float(score)
        })

    return {"results": response_data}

app.mount("/data", StaticFiles(directory="data"), name="data")