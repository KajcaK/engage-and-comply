🌱 Green Hackathon Project — Readable AI: Turn Complex PDFs into Cool Stories

Theme: Engage and Comply
Making sustainability documents more accessible, engaging, and human.

📘 Overview

Readable AI is a web platform developed for the Green Hackathon with the mission to transform dense sustainability or compliance-related PDFs into simplified and engaging narratives using Large Language Models (LLMs).  

Whether it’s an environmental report or a CSR strategy document, our platform helps users—especially non-technical stakeholders—understand the key takeaways in a fun, narrative format.

🎯 Objective

✅ Empower compliance through engagement  
✅ Break down complex documents into stories  
✅ Improve readability and comprehension of green initiatives  

💻 How It Works

1. The user uploads a PDF document via the platform.
2. The backend processes the content using LangChain and LLMs.
3. The LLM generates a story-like summary from the original content.
4. The summary is displayed in a friendly chat interface and structured narrative view.

🧰 Tech Stack

🌐 Frontend
- React.js: Interactive UI
- Bootstrap: Styling and layout
- ChatContainer.jsx and StoryContainer.jsx: Components for chat interaction and story display

🧠 Backend
- Python with FastAPI: Handles PDF processing and LLM communication
- LangChain: Chains LLMs with PDF data
- OpenAI or HuggingFace Models: Generates human-friendly summaries
- PyMuPDF / pdfplumber: For PDF text extraction
- LangServe: Exposes LangChain pipelines as HTTP APIs

📦 Requirements
Key dependencies listed in requirements.txt include:
- langchain
- fastapi
- openai or huggingface
- pymupdf
- uvicorn (server)
- aiofiles, httpx, dotenv, etc.

### 🚀 Getting Started

1. **Clone the repository**
   ```bash
   git clone https://github.com/your-username/readable-ai.git
   cd readable-ai
   ```

2. **Backend setup**
   ```bash
   python -m venv venv
   source venv/bin/activate  # Windows: venv\Scripts\activate
   pip install -r requirements.txt
   ```

3. **Run the FastAPI server**
   ```bash
   uvicorn server:app --reload
   ```

4. **Frontend setup**  
   In the `/frontend` folder (assuming Vite or similar setup):
   ```bash
   npm install
   npm run dev
   ```


🧪 Sample Workflow

1. User uploads a PDF about "Carbon Footprint Management".
2. The LLM reads the document and outputs a story like:
   "Once upon a time, a company wanted to shrink its carbon shadow..."
3. The result is displayed in two formats:
   - Conversational style (chat bubble)
   - Structured Q&A/story breakdown

🌍 Why It Matters

By simplifying technical language and turning data into stories, we help organizations:
- Increase employee engagement
- Improve green initiative comprehension
- Enhance compliance through transparency

🙌 Team & Contribution

Built with love during the Green Hackathon 💚  
We welcome contributions! Open an issue or pull request to collaborate.
