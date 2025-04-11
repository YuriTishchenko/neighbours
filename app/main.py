from fastapi import FastAPI

app = FastAPI(title='Neighbours API')

@app.get('/')
async def root():
    return {'message': 'Hi neighbours!'}