import os            #provide access to systems directories
import shutil        #provides functions for file operations such as copying and moving
from Config.dbconfig import MYSQL_HOST, MYSQL_PORT, MYSQL_USER, MYSQL_PASSWORD, MYSQL_DB     #import the required datas from dbconfig file
import mysql.connector as db     #mysql connector is used to provide connection with db
from fastapi import FastAPI, File, UploadFile, APIRouter   #import components needed to create fastapi applications 
from sentence_transformers import SentenceTransformer      #sentence transformer is a class used for transforming sentenses to vectors
from langchain_community.document_loaders import DirectoryLoader   #this class used for loading documents from a directory
from langchain_community.document_loaders import PyPDFLoader       
from langchain.text_splitter import RecursiveCharacterTextSplitter  #this class used for splitting text to chunks
from pinecone import Pinecone        #loading class for vector db

app = FastAPI()      #create fastapi application instance used for creating APIs
conn = db.connect(host=MYSQL_HOST, user=MYSQL_USER, password=MYSQL_PASSWORD, database=MYSQL_DB, port=MYSQL_PORT)
cursor = conn.cursor()   #establishing database connection

directory = "./docu"     #directory for storing pdf documents
if not os.path.exists(directory):  #if such a directory not exist create a directory
    os.makedirs(directory)

router = APIRouter()        #routers for defining apis

model = SentenceTransformer("all-MiniLM-L6-v2")  #models used totransform text to vectors
index_name = 'your_pinecone_index_name'    
pc = Pinecone(api_key="your_pinecone_api_key")
index = pc.Index(index_name)
# function used for loading pdfs
def load_docs(file):
    try:
        loader=DirectoryLoader(file,glob = "./*.pdf",loader_cls=PyPDFLoader)  #loading the pdf files
        documents=loader.load()
        return documents   #documents contents where loaded
    except Exception as e:
        print(f"An error occurred while loading documents: {e}")  #to handle errors or exceptions 

# function used for splitting text
def split_docs(documents, chunk_size=500, chunk_overlap=20):
    try:
        text_splitter = RecursiveCharacterTextSplitter(chunk_size=chunk_size, chunk_overlap=chunk_overlap)
        docs = text_splitter.split_documents(documents) #texts split into vectors
        # print(docs)
        return docs

    except Exception as e:
        print(f"An error occurred while splitting the  documents: {e}")


@router.post("/upload")  #creating an api for uploading the pdf
async def upload_pdf(file: UploadFile = File(...)):  #fuction for uploading the pdf
    try:
        items = []
        if file.content_type != "application/pdf":  #only pdf docu are allowed
            return {"error": "Only PDF files are allowed."}
        filename = file.filename    #loading file name
        file_loc = directory + "/" + filename   #loading file location
        with open(file_loc, "wb") as buffer:   #open file in write mode
            shutil.copyfileobj(file.file, buffer) #shares the uploaded file into specified location
        if os.path.exists(directory):  #if such a directory exists load them
            docs = load_docs(directory)
            #docs = load_docs(file_loc)
            for i, chunk in enumerate(docs):#loading chunks from docs
                doc_id = str(i)      #id for chunks
                embedding = model.encode(chunk.page_content).tolist() #convert the chunks to numerical representation
                print(embedding)
                metadata = {"content": chunk.page_content} #creates a dictionary called metadata containing metadata information about the chunk.
                items.append({"id": doc_id, "values": embedding, "metadata": metadata}) #This line creates a dictionary representing chunk id,values,metadata
                try:
                    index.upsert(vectors=items)  #update and insert the chunks
                except Exception as e:
                    return {"error": str(e)}

        return {"filename": filename, "content_type": file.content_type,   
                "sample": f"Upserted {len(items)} items to Pinecone index '{index_name}'."}#after uploading it returns these values
    except Exception as e:
        print(e)
        return {"error": e}