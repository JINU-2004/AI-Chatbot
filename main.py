from fastapi import FastAPI,Request   #The main class of the FastAPI framework used to create the web application.
from fastapi.middleware.cors import CORSMiddleware   #Middleware for handling Cross-Origin Resource Sharing (CORS) policies.
from middle_ware.users import login     
from middle_ware.edith_model import chatbot_data_manager,chatbot

from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles      # Middleware for serving static files such as CSS, JavaScript, and images.
from fastapi.templating import Jinja2Templates   # Templating engine for generating HTML responses

origins = ["*"]        #"origin" refers to the combination of scheme (protocol), domain, and port from which a web resource originates.
app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")    #Mount the "/static" directory to serve static files, such as CSS and JavaScript
templates = Jinja2Templates(directory="templates")        #Initialize the Jinja2Templates engine to render HTML templates from the "templates" directory.
@app.get("/index", response_class=HTMLResponse)           #Define a route handler for the "/index" endpoint to serve the index.html template.
async def read_item(request: Request):                    #Define an asynchronous function read_item() that takes a Request object.
    return templates.TemplateResponse(                    ##Return a TemplateResponse with the rendered "index.html" template
        request=request, name="index.html"
    )
app.add_middleware(CORSMiddleware,                        #These middleware components may handle tasks such as user authentication (login middleware) or interact with external models for chatbot functionality 
                   allow_origins=origins,                 # specifies which origins are allowed to access resources served by the FastAPI application
                   allow_credentials=True,                #user credentials are included with the request
                   allow_methods=["*"],                   #allows all HTTP methods (GET, POST, etc.) to be used in cross-origin requests.
                   allow_headers=["*"],)                  # allows all headers to be included in cross-origin requests.

#Admin login creation
@app.get("/login", response_class=HTMLResponse)
async def read_item(request: Request):
    return templates.TemplateResponse(
        request=request, name="login.html"
    )
@app.get("/upload", response_class=HTMLResponse)        #upload page creation
async def read_item(request: Request):
    return templates.TemplateResponse(
        request=request, name="upload.html"
    )
#handle API related to user authentication, PDF management, and chatbot functionality.
app.include_router(login.router, prefix="/api", tags=["Authentication"])
app.include_router(chatbot_data_manager.router, prefix="/api", tags=["Pdf-Management"])
app.include_router(chatbot.router, prefix="/api", tags=["Chatbot"])