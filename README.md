# A.C.E

This project has been done during the [GreenHack 2025](https://greenhack.eu/) hackathon on 30-31th of May 2025 by this repo's collaborators as a solution to the *Engage & Comply* challenge from Novartis.

**A.C.E.** -- AI for Compliance Engagement. The project is an LLM-based web application that takes a (large and information-dense) PDF file as an input, and transforms it into a series of case studies for easy learning of compliance standards and documentation. The program uses LangChain and an LLM with RAG to process documents and interact with the user.

## Workflow

1. The user uploads a PDF document via the platform.
2. The backend processes the content using LangChain and LLMs.
3. The LLM generates a story-like summary from the original content and retells it through the chat interface, also asking the user for engagement.

## Future plans

1. Add the capability to show a report of how much of the material has been covered.
2. Add learning assessments
3. Support citation of document paragraphs when giving the information to the user
4. Use a smaller model for running locally

## Technologies

### 🌐 Frontend
- React.js: Interactive UI
- Django: Backend REST API
- Langserve & FastAPI: LLM Server
- LangChain
- Featherless API: Serverless running of the LLM
- Qdrant: Vector database

### 🧠 Backend
- LangChain: Chains LLMs with PDF data
- GLM-4-32B-0414: LLM
- PyMuPDF / pdfplumber: For PDF text extraction
- LangServe: Exposes LangChain pipelines as HTTP APIs


## Usage

### Requirements

Install requirements listed in the `requirements.txt` file: `pip install -r requirements` (recommended to run in a python venv). Some of the key requirements are:
- langchain (langchain-qdrant, langchain-openai...)
- fastAPI
- PyPDF2
- uvicorn (server)

### Running

TODO

