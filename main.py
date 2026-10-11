from fastapi import FastAPI, Path, HTTPException, Query
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
        raise HTTPException(status_code=404, detail="Patient not found")

@app.get("/sort")
def sort_patients(sort_by: str = Query(..., description="sort on the basis of bmi, height, weight"), order: str = Query("asc", description="Order of sorting: asc or desc")):
    valid_field = ["bmi", "height", "weight"]
    if sort_by not in valid_field:
        raise HTTPException(status_code=400, detail="Invalid sort_by parameter")

    if order not in ["asc", "desc"]:
        raise HTTPException(status_code=400, detail="Invalid order parameter")

    data = load_data()
    sort_order = True if order == "desc" else False
    sorted_data = sorted(data.values(), key=lambda x: x[sort_by], reverse=sort_order)
    return sorted_data
