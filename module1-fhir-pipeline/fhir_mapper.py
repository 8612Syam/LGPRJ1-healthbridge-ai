import json
from datetime import datetime, timezone
from fhir.resources.observation import Observation
from fhir.resources.quantity import Quantity
from fhir.resources.codeableconcept import CodeableConcept
from fhir.resources.coding import Coding

def map_obx_to_fhir(obx_data):
    """
    Transforms a single OBX dictionary into a FHIR R4 Observation JSON.
    """
    # 1. Initialize the FHIR Observation resource
    observation = Observation(
        status=obx_data["status"].lower(), 
        category=[{
            "coding": [{
                "system": "http://terminology.hl7.org/CodeSystem/observation-category",
                "code": "vital-signs",
                "display": "Vital Signs"
            }]
        }],
        code={
            "coding": [{
                "system": "http://loinc.org",
                "code": obx_data["loinc"],
                "display": obx_data["name"]
            }]
        }
    )

    # 2. Add the Value as a FHIR Quantity
    observation.valueQuantity = Quantity(
        value=float(obx_data["value"]),
        unit=obx_data["units"],
        system="http://unitsofmeasure.org",
        code=obx_data["units"]
    )

    # 3. Add a timestamp with the 'Z' (Zulu/UTC) suffix required by FHIR
    observation.effectiveDateTime = datetime.now(timezone.utc).isoformat().replace("+00:00", "Z")

    return observation.json(indent=2)

if __name__ == "__main__":
    sample_obx = {
        "name": "Glucose",
        "loinc": "2345-7",
        "value": "95",
        "units": "mg/dL",
        "status": "Final"
    }

    print("--- Mapping HL7 OBX to FHIR R4 ---")
    fhir_json = map_obx_to_fhir(sample_obx)
    print(fhir_json)
    
    with open("module1-fhir-pipeline/sample_fhir_output.json", "w") as f:
        f.write(fhir_json)
    print("\n✅ Success! Saved to module1-fhir-pipeline/sample_fhir_output.json")