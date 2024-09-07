from ninja import NinjaAPI, Schema

api = NinjaAPI()


class UserSchema(Schema):
    username: str
    is_authenticated: bool
    email: str = None


@api.get("/fa")
def hello(request):
    return "Hello, world!"


@api.get("/me", response=UserSchema)
def me(request):
    return request.user
