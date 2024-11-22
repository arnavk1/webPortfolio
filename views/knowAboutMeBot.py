import os 
import streamlit as st
import cassio
import ast
from dotenv import load_dotenv
from langchain_huggingface import HuggingFaceEndpoint
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.indexes.vectorstore import VectorStoreIndexWrapper
from langchain_community.vectorstores import Cassandra
from langchain.llms import OpenAI
from PyPDF2 import PdfReader
from langchain.embeddings import OpenAIEmbeddings
from typing_extensions import Concatenate

load_dotenv()

os.environ["LANGCHAIN_API_KEY"] = os.getenv("LANGCHAIN_API_KEY")
os.environ["LANGCHAIN_TRACING_V2"] = "true"
os.environ["LANGCHAIN_PROJECT"] = "Portfolio Website Using Gen-AI Concept"
ASTRA_DB_TOKEN=os.getenv("ASTRA_DB_TOKEN")
ASTRA_DB_ID=os.getenv("ASTRA_DB_ID")
hf_token = os.getenv("HF_Token")
OPENAI_API_KEY=os.getenv("OPENAI_API_KEY")

cassio.init(token=ASTRA_DB_TOKEN,database_id=ASTRA_DB_ID)

# prompt = ChatPromptTemplate.from_template(
#     """
#     You are friend of Arnav. Your name is Ibot. You have to answer user query like that.
#     Answer the questions based on the provided context only.
#     Please provide the most accurate response based on the question.
#     Refrain from providing answers outside of context.
#     Give only single top result as output.
    
#     Question:{question}
#     """
# )


repo_id="meta-llama/Llama-3.2-11B-Vision-Instruct"
llm = OpenAI(openai_api_key=OPENAI_API_KEY)
#HuggingFaceEndpoint(repo_id=repo_id,max_length=150,temperature=0.7,token = hf_token)
embeddings = OpenAIEmbeddings(openai_api_key=OPENAI_API_KEY)
# HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2",num_dimensions=1536)
pdfReader=PdfReader('Utilities\ArnavResume2024.pdf')


def create_vec_db(question):
    raw_text = ''
    for i,page in enumerate(pdfReader.pages):
        content=page.extract_text()
        if content:
            raw_text+=content
    cassio.init(token=ASTRA_DB_TOKEN,database_id=ASTRA_DB_ID)
    
    astra_vector_store=Cassandra(
        embedding=embeddings,
        table_name='qa_mini_demo',
        session=None,
        keyspace=None
    )
    
    
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=200,
        chunk_overlap=50,
    )
    texts = text_splitter.split_text(raw_text)
    astra_vector_store.add_texts(texts[:50])
    print("Inserted %i headlines. "% len(texts[:50]))

    astra_vector_index=VectorStoreIndexWrapper(vectorstore=astra_vector_store)
    answer = astra_vector_index.query(question, llm=llm).strip()
    # print(answer)
    return answer

def generating_response(question):
    
    
    answer = create_vec_db(question)
    return answer
    # print("\nAnswer: \"%s\""% answer)
    
    # print(type(answer))
    # return answer[0]

st.title("Ask About Me!")


st.write("Ask anything!!")
question = st.text_input("Write your query...")


if question:
    st.write(generating_response(question))
else:
    st.write("Please provide a query")