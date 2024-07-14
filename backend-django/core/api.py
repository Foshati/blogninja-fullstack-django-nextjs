from ninja import NinjaAPI

app = NinjaAPI()


@app.get("/fa")
def hello(request):
    return "Hello, world!"




