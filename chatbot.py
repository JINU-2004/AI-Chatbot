import json    #javascript object notation
from fastapi import APIRouter
from Schema.all_schema import chatbot_respose
from fastapi.encoders import jsonable_encoder as je
from sentence_transformers import SentenceTransformer
from pinecone import Pinecone
import google.generativeai as genai
router = APIRouter()   #Creates an APIRouter instance, which is a class from FastAPI used to define API endpoints.
model = SentenceTransformer("all-MiniLM-L6-v2")
index_name = 'your_pinecone_index_name'
pc = Pinecone(api_key="your_pineconedb_api_key")
index = pc.Index(index_name)
gemini_api_key = "your_geminimodel_api_key"
genai.configure(api_key=gemini_api_key)  #Configures or attaches the generative AI (Gemini) by providing the API key.

safety_settings = "{}" #ensures safety for gemini model
safety_settings = json.loads(safety_settings)
gemini = genai.GenerativeModel(model_name="gemini-pro", safety_settings=safety_settings)

def gemini_processor(list_data,query):  #Defines a function to process requests using the generative AI (Gemini) model
    try:
        list_data.append("summarize this list of text and give a short accurate output for the question" + query+".please dont make incorrect answer")
        prompt_text = "\n".join(list_data)
        response = gemini.generate_content(prompt_text)  #generate response for the query
        if response.text:
            return response.text
    except Exception as e:
        return {"error Gemini": str(e)}

def pineconePocessor(queries):  #Defines a function to process requests using the Pinecone vector index
    try:
        query_embedding = model.encode(queries).tolist()
        if query_embedding:
            query_response = index.query(
                include_values=True,
                include_metadata=True,
                include_entities=True,
                include_scores=True,#parameters are set to True to include additional information in the query response.
                include_links=True,
                top_k=1,             #top_k specifies the maximum number of nearest neighbors to retrieve
                temperature=0,
                vector=[query_embedding]
            )
            results = []
            for item in query_response["matches"]:
                result = item["metadata"]["content"]#This block iterates over the matches returned by the query response and extracts the content metadata associated with each match
                results.append(result)#It then appends the content to the results list.
            return results
        else:
            return {"error": "The server is down! Please contact your administrator"}
    except Exception as e:
        return {"error Pinecone": str(e)}

@router.post("/chatbot")
def chatbot(chat:chatbot_respose):   #chatbot user queries are oaded here
    try:
        chat_data = je(chat)  #encode the chat in the dictionary format
        list = pineconePocessor(chat_data["chat"]) #lists corresponding to these chat is loaded into list
        chat_response = gemini_processor(list,chat_data["chat"])   #call gemini function to get the response
        return {"chat": str(chat_response)} 
    except Exception as e:
        print("Exception:", e)
        return {"error Chatbot": str(e)}