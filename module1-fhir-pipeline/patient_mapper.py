import json
from fhir.resources.patient import Patient
from fhir.resources.humanname import HumanName
from fhir.resources.identifier import Identifier

def map_pid_to_fhir(patient_data):
    """
    Transforms PID data into a FHIR R4 Patient JSON.
    """
    patient = Patient()
    
    # 1. Add Patient ID
    patient.identifier = [Identifier(value=patient_data["id"])]
    
    # 2. Add Name
    name = HumanName()
    name.family = patient_data["last_name"]
    name.given = [patient_data["first_name"]]
    patient.name = [name]
    
    # 3. Add Gender and DOB
    patient.gender = "male" if patient_data["gender"] == "M" else "female"
    # Format YYYYMMDD to YYYY-MM-DD
    dob = patient_data["dob"]
    patient.birthDate = f"{dob[:4]}-{dob[4:6]}-{dob[6:]}"

    return patient.json(indent=2)

if __name__ == "__main__":
    # Data from your successful parse_hl7.py run
    sample_patient = {
        "id": "PAT001",
        "first_name": "JOHN",
        "last_name": "SMITH",
        "dob": "19800315",
        "gender": "M"
    }

    print("--- Mapping HL7 PID to FHIR Patient ---")
    patient_json = map_pid_to_fhir(sample_patient)
    print(patient_json)
    
    with open("module1-fhir-pipeline/sample_patient_fhir.json", "w") as f:
        f.write(patient_json)
    print("\n✅ Success! Saved to module1-fhir-pipeline/sample_patient_fhir.json")