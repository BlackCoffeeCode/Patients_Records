from fastapi import FastAPI, Path
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

@app.get("/patient/{patient_id}")
def view_patient(patient_id: str = Path(..., description="The ID of the patient to retrieve", example="SAMPLE001")):
    data = load_data()
    if patient_id in data:
        return data[patient_id]
    else:
        return {"error": "Patient not found."}
