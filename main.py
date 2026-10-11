from fastapi import FastAPI
import uvicorn
import json

app = FastAPI()

def load_data():
    with open("patients.json", "r") as f:
        data = json.load(f)
    return data

@app.get("/")
def Hello():
    return {"message": "My name is Patient Records API."}

@app.get("/about")
def about():
    return {"message": "This is a patient records API."}

@app.get("/view")
def view():
    data = load_data()
    return data
