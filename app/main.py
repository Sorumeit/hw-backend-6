from fastapi import Cookie, FastAPI, Form, Request, Response, templating
from fastapi.responses import RedirectResponse

from .flowers_repository import Flower, FlowersRepository
from .purchases_repository import Purchase, PurchasesRepository
from .users_repository import User, UsersRepository

from jose import jwt

app = FastAPI()
templates = templating.Jinja2Templates("templates")


flowers_repository = FlowersRepository()
purchases_repository = PurchasesRepository()
users_repository = UsersRepository()

def create( id : int ) -> str:
    user = { "used_id" : id }
    token = jwt.encode( user , "nfactorial" , "HS256" )
    return token

def decode( token : str ) -> int:
    id = jwt.decode( token , "nfactorial" , "HS256" )
    return id["user_id"]

@app.get("/")
def root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.get("/signup")
def signup( request : Request ):
    return templates.TemplateResponse (
        "sign.html",
        {
            "request" : request
        }
    )

@app.post("/signup")
def sign( request : Request,
    email : str = Form() , 
    fullname : str = Form() , 
    password : str = Form() 
     ):
    new_user = {
        "email" : email,
        "fullname" : fullname,
        "password" : password
    }
    users_repository.add( new_user )
    return RedirectResponse( "/login" , status_code = 303 )

@app.get("/login")
def log( request : Request ):
    return templates.TemplateResponse(
        "login.html",
        {
            "request" : request
        }
    )


@app.post("/login")
def login( request : Request ,
          email : str = Form(),
          password : str = Form() ):
    ans = users_repository.check( email , password )
    if ( ans == 0 ):
        return RedirectResponse ( "/login" , status_code = 303 )
    response = RedirectResponse( "/profile" , status_code = 303 )
    token = create( ans )
    response.set_cookie( "token" , token )
    return response

@app.get( "/profile" )
def profile( request : Request,
            token : str = Cookie(),
         ):
    id = decode( token )
    user = users_repository.get( id )
    return templates.TemplateResponse( 
        "profile.html",
        {
            "request" : request,
            "user" : user
        }
    )

