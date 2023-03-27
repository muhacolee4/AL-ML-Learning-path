from fastapi import FastAPI

app=FastAPI()
@app.get("/root")
def read_root():
    return {"Hello":"World"}