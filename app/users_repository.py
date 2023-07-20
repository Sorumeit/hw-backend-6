from attrs import define


@define
class User:
    email: str
    full_name: str
    password: str
    id: int = 0


class UsersRepository:
    users: list[User]

    def __init__(self):
        self.users = []
    
    def add( self , user ):
        new = User
        new.email = user["email"]
        new.full_name = user["fullname"]
        new.password = user["password"]
        new.id = len( self.users ) + 1
        self.users.append( new )
