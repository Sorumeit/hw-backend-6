from fastapi import Cookie, FastAPI, Form, Request, Response, templating
from fastapi.responses import RedirectResponse

from .flowers_repository import Flower, FlowersRepository
from .purchases_repository import Purchase, PurchasesRepository
from .users_repository import User, UsersRepository

app = FastAPI()
templates = templating.Jinja2Templates("templates")


flowers_repository = FlowersRepository()
purchases_repository = PurchasesRepository()
users_repository = UsersRepository()


@app.get("/")
def root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.get("/signup")
def signup( request : Request ):
    return templates.TemplateResponse (
        "/signup/sign.html",
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
