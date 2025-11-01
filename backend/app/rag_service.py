import os
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import Chroma
from langchain.text_splitter import CharacterTextSplitter
from langchain.chat_models import ChatOpenAI
from langchain.chains import RetrievalQA

PERSIST_DIR = os.environ.get("CHROMA_PERSIST_DIR", "./chroma_db")

def build_or_get_vectordb(documents: list[str]):
    splitter = CharacterTextSplitter(chunk_size=800, chunk_overlap=100)
    chunks = []
    for d in documents:
        chunks.extend(splitter.split_text(d))

    embeddings = OpenAIEmbeddings()
    vectordb = Chroma(persist_directory=PERSIST_DIR, embedding_function=embeddings)

    try:
        if vectordb._collection.count() == 0:
            vectordb.add_texts(chunks)
            vectordb.persist()
    except Exception:
        vectordb = Chroma.from_texts(chunks, embeddings, persist_directory=PERSIST_DIR)
        vectordb.persist()

    return vectordb

def answer_with_rag(question: str, vectordb: Chroma):
    llm = ChatOpenAI(temperature=0)
    retriever = vectordb.as_retriever(search_kwargs={"k": 3})
    qa = RetrievalQA.from_chain_type(llm=llm, chain_type="stuff", retriever=retriever)
    result = qa.run(question)
    return result
