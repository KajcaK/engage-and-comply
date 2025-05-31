from dotenv import load_dotenv
import os

from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI
from langserve import add_routes

from langchain_openai import ChatOpenAI
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_qdrant import QdrantVectorStore
from langchain.chains import RetrievalQA
from langchain_core.prompts import PromptTemplate
from langchain.memory import ChatMessageHistory
from langchain_core.runnables import (
    RunnableLambda,
    RunnablePassthrough,
    RunnableParallel,
)
from langchain_core.runnables.history import RunnableWithMessageHistory
from operator import itemgetter

# Load environment variables
load_dotenv()

print("🔧 Starting server setup...")

app = FastAPI()

origins = ["http://127.0.0.1:5173", "http://127.0.0.1:8000"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,          # or ["*"] for dev
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Load models
api_key = os.getenv("OPENAI_API_KEY")

llm = ChatOpenAI(
    api_key=api_key,
    base_url="https://api.featherless.ai/v1",
    model="THUDM/GLM-4-32B-0414",
)
print("✅ LLM loaded")

embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-mpnet-base-v2")
print("✅ Embedding model loaded")

try:
    vectorstore = QdrantVectorStore.from_existing_collection(
        collection_name="pdf_file",
        url=os.getenv("QDRANT_URL"),
        api_key=os.getenv("QDRANT_API_KEY"),
        embedding=embeddings
    )
    print("✅ Vectorstore connected")
except Exception as e:
    print("❌ Failed to connect to vectorstore:", e)
    raise RuntimeError("❌ Collection 'pdf_file' not found. Run 'indexer.py' first to create it.") from e

retriever = vectorstore.as_retriever()
print("✅ Retriever ready")

custom_prompt = PromptTemplate.from_template("""
AI Teaching Assistant Prompt Template
ROLE: You are an AI teaching assistant. Your role is to guide a student through an educational document in an engaging and interactive way. You should teach only from the contents of the provided PDF and not use any outside information or search tools.
OBJECTIVE: Break down the document into sequential learning parts (chapters or missions). Present each part as a chapter in a story or narrative (e.g., detective story, space mission, fantasy quest) to keep learners engaged. At the end of each part, ask a quiz-style question to test comprehension.
RULES:
Use only the content from the provided PDF.
Present content in small, engaging, story-like chunks.
End each section with a multiple-choice quiz question (4 options).
If the student answers incorrectly, reframe the question and encourage them.
On correct answers, provide a short affirmation and a brief explanation (with the option to "Learn More").
Use clear formatting: chapter headers, bullet points, and quizzes.
Do not summarize large sections—guide interactively instead.
TEMPLATE STRUCTURE:
Chapter [#]: [Creative Chapter Title] Story-based setup that introduces a key theme or concept from the document.
Core Lesson Content:
[Teach the key point(s) clearly and concisely. Use bullets or simple explanation.]
Quiz Time: What is [core concept]? A) [Option 1]
B) [Option 2]
C) [Option 3]
D) [Option 4]
Wait for student’s answer and respond accordingly:
:white_check_mark: Correct: Provide encouragement + brief recap. Ask if they want to explore more.
:x: Incorrect: Gently rephrase the question and encourage retrying.
EXAMPLE USAGE: Applied to a document on carbon accounting:
Chapter 1: "The Case of the Vanishing Data"
Core Concept: Scope 3 emissions are hard to track due to poor data quality.
Quiz: What is the biggest challenge in Scope 3 accounting?
Write in plain text, no markdown or code blocks. Tell the story in shorter sections, each a few sentences long, and provoke the student to think and provide their thoughts.

Context:
{context}

Question:
{question}

Answer:
""")

qa_chain = RetrievalQA.from_chain_type(
    llm=llm,
    retriever=retriever,
    chain_type_kwargs={"prompt": custom_prompt}
)
print("✅ QA chain ready")

# Util function to extract text from different input formats
def extract_query(input_data):
    if isinstance(input_data, list):
        return input_data[-1].content
    elif hasattr(input_data, 'content'):
        return input_data.content
    return input_data

# Final chain using LCEL and support for chat history
chain_final = (
    RunnableParallel({
        "input": itemgetter("input") | RunnableLambda(extract_query),
        "history": itemgetter("history")
    })
    | RunnableLambda(lambda x: {"query": x["input"]})
    | qa_chain
)

# Use LangChain's default ChatMessageHistory to fix stream_log compatibility
def get_session_history(session_id: str):
    return ChatMessageHistory()

runnable_with_history = RunnableWithMessageHistory(
    chain_final,
    get_session_history,
    input_messages_key="input",
    history_messages_key="history",
)

try:
    add_routes(app, runnable_with_history, path="/chat")
    print("✅ Routes added successfully")
except Exception as e:
    print("❌ Failed to add routes:", e)
    raise

@app.get("/")
def health_check():
    return {"status": "ok"}
