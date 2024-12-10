from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def postData():
    return {"data": {"name": "harsh"}}


@app.get("/about")
def postAbout():
    return {"AboutData": {"name": "harsh", "worktype": "Software Engineer Web Dev"}}
