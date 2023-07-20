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

    def check( self , email , password ):
        ans = 0
        for i in range( len( self.users ) ):
            if ( self.users[i].email == email and self.users[i].password == password ):
                ans = self.users[i].id
        return ans
    
    def get( self , id ):
        for i in range( len( self.users ) ):
            if ( self.users[i].id == id ):
                return self.users[i]
