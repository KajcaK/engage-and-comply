#!/usr/bin/env python3

from langchain_community.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import PyPDFLoader
from langchain_qdrant import QdrantVectorStore
from qdrant_client import QdrantClient
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough, RunnableParallel
from langchain_featherless_ai import ChatFeatherlessAi
from langchain_openai import ChatOpenAI


import os
api_key = os.getenv("OPENAI_API_KEY")  # Ainda usado para LLM se quiser
debug = os.getenv("DEBUG")


def create_rag_chain(llm, retriever, rag_prompt):
    def format_docs(docs):
        return "\n\n".join(doc.page_content for doc in docs)

    rag_chain_from_docs = (
        RunnablePassthrough.assign(context=(lambda x: format_docs(x["documents"])))
        | rag_prompt
        | llm
        | StrOutputParser()
    )

    rag_chain_with_source = RunnableParallel(
        {"documents": retriever, "question": RunnablePassthrough()}
    ).assign(answer=rag_chain_from_docs)

    return rag_chain_with_source

def start_session(filename: str):
    try:
        loader = PyPDFLoader(f"./backend/fixtures/{filename}")
        documents = loader.load()
    except Exception as e:
        print(f"Error preparing or loading document: {e}")
        documents = []

    retriever = None
    if documents:
        text_splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
        split_docs = text_splitter.split_documents(documents)

        # Using a common, reliable sentence transformer model
        embeddings_model_name = "sentence-transformers/all-mpnet-base-v2"
        embeddings = HuggingFaceEmbeddings(model_name=embeddings_model_name)

        QdrantVectorStore.from_documents(
            documents=documents,
            embedding=embeddings,
            api_key=os.getenv("QDRANT_API_KEY"),
            url=os.getenv("QDRANT_URL"),
            prefer_grpc=True,
            collection_name=filename
        )

        #client = QdrantClient(url=os.getenv("QDRANT_URL"))
        #client.get_collection("{filename}")

        try:
            vectorstore = FAISS.from_documents(split_docs, embeddings)
            retriever = vectorstore.as_retriever(search_kwargs={"k": 2})
        except Exception as e:
            print(f"Error creating FAISS vector store or retriever: {e}")
    else:
        print("No documents loaded, retriever will not be initialized.")



    # Initialize Featherless LLM
    llm = ChatOpenAI(
        api_key=os.getenv("FEATHERLESS_API_KEY"),
        base_url="https://api.featherless.ai/v1",
        model="THUDM/GLM-4-32B-0414",
       )
    #llm = ChatFeatherlessAi(
    #    featherless_api_key=os.getenv("FEATHERLESS_API_KEY"),
    #    model="mistralai/Mistral-Small-24B-Instruct-2501",
    #    temperature=0.3
    #   )


    # RAG Prompt Template
    template = """Write 5 questions about the core elements and highlights of the following text:
    {context}

    Answer:"""
    rag_prompt = ChatPromptTemplate.from_template(template)

    # Helper function to format retrieved documents

    if retriever:
        # Construct the RAG chain using LCEL

        rag_chain_with_source = create_rag_chain(llm, retriever, rag_prompt)

        # Example Invocation
        #question = "By what kinds of stakeholders should the PACT methodology be applied?"
        result = rag_chain_with_source.invoke("")

        #print(f"\nQuestion: {question}")
        print(f"Answer: {result['answer']}")
        print("\nSources:")
        for doc in result['documents']:
            print(f"- {doc.page_content} (Metadata: {doc.metadata})")
        return result

    else:
        print("RAG chain not created as retriever is unavailable.")


if __name__== "__main__":
    start_session("pact-methodology.pdf")
