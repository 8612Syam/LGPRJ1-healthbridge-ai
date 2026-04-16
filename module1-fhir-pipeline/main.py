from fastapi import FastAPI, HTTPException
import sys
import os

# Ensures the current directory is in the path for imports
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from fhir_mapper import map_obx_to_fhir

app = FastAPI(
    title="HealthBridge AI — FHIR Pipeline",
    description="API for transforming HL7 v2 to FHIR R4",
    version="1.0.0"
)

@app.get("/")
def read_root():
    return {"status": "HealthBridge AI Module 1 is Online"}

@app.post("/observations/transform")
def transform_observation(name: str, loinc: str, value: float, units: str):
    try:
        data = {"name": name, "loinc": loinc, "value": value, "units": units, "status": "Final"}
        return map_obx_to_fhir(data)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)