from fastapi import FastAPI
app=FastAPI(title="this is my fast api Demo")
@app.get('/{demo}')
def hello(demo):
    return f"hello{demo}"
@app.post('/hesa/hesa')
async def hesa(user):
    return user.name