from fastapi import FastAPI



app = FastAPI()


@app.get('/')
async def test():
    return {'hello': 'hello from fastapi'} 