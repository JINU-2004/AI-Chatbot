from fastapi import APIRouter,Form,Request,status
from Schema.all_schema import login_respose
from Config.dbconfig import MYSQL_HOST, MYSQL_PORT, MYSQL_USER, MYSQL_PASSWORD,MYSQL_DB
import mysql.connector as db
import jwt
from fastapi.encoders import jsonable_encoder as je
from fastapi.templating import Jinja2Templates
#from fastapi.responses import HTMLResponse
from fastapi.responses import RedirectResponse
router = APIRouter()
templates = Jinja2Templates(directory="templates")
conn = db.connect(host = MYSQL_HOST,user = MYSQL_USER,
                  password =MYSQL_PASSWORD,database = MYSQL_DB,
                  port = MYSQL_PORT)

cursor = conn.cursor()

SECRET_KEY = "DAK"
ALGORITHM = "HS256"

@router.post("/login")
#def login(user:login_respose):
async def login(request:Request, username:str = Form(...), password:str = Form(...)):
    try:
        #user_dict = je(user)
        #_username = user_dict["username"]
        #_password = user_dict["password"]
        _username=username
        _password=password
        cursor.execute("SELECT * FROM tbl_user WHERE BINARY username = %s and password = %s ",(_username,_password))
        account = cursor.fetchone()
        if account:
            #token_json = {"username":_username}
            #token = jwt.encode(token_json,SECRET_KEY,algorithm=ALGORITHM)   and status=1
            #cursor.execute("UPDATE `tbl_users` SET `jwt_token` = %s WHERE username = %s",(token,_username))
            #conn.commit()
            #response = {"Tokon":token,"username":_username}
            
            return RedirectResponse(url="http://127.0.0.1:8000/upload",status_code=status.HTTP_303_SEE_OTHER)
        else:
            return {"message":"Invalid username or password"}
    except Exception as e:
        print(e)
