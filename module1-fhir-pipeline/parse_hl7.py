"""
HealthBridge AI — Module 1
parse_hl7.py

Parses a sample HL7 v2 ORU^R01 message.
Extracts PID (patient) and OBX (observation) segments.
Prints structured output to console.

Week 2 deliverable — github.com/8612Syam/LGPRJ1-healthbridge-ai
"""

from hl7apy.core import Message
from hl7apy import parser

# ── Sample HL7 v2 ORU^R01 message ───────────────────────────────────────────
SAMPLE_HL7 = (
    "MSH|^~\\&|LAB|HOSPITAL|EHR|CLIENT|20240101120000||ORU^R01|MSG001|P|2.5\r"
    "PID|1||PAT001^^^HOSPITAL^MR||SMITH^JOHN^A||19800315|M|||123 MAIN ST^^MASON^OH^45040||5551234567\r"
    "OBR|1|ORD001|LAB001|85025^CBC^LN|||20240101110000\r"
    "OBX|1|NM|8867-4^Heart rate^LN||72|/min|60-100||||F|||20240101110000\r"
    "OBX|2|NM|8480-6^Systolic blood pressure^LN||120|mm[Hg]|90-120||||F|||20240101110000\r"
    "OBX|3|NM|2345-7^Glucose^LN||95|mg/dL|70-100||||F|||20240101110000\r"
    "OBX|4|NM|718-7^Hemoglobin^LN||14.2|g/dL|12.0-17.5||||F|||20240101110000\r"
)

def parse_pid(pid_segment):
    """Extract patient demographics from PID segment."""
    fields = pid_segment.split("|")
    patient = {
        "patient_id":   fields[3].split("^")[0] if len(fields) > 3 else "",
        "last_name":    fields[5].split("^")[0] if len(fields) > 5 else "",
        "first_name":   fields[5].split("^")[1] if len(fields) > 5 and len(fields[5].split("^")) > 1 else "",
        "date_of_birth": fields[7] if len(fields) > 7 else "",
        "gender":       fields[8] if len(fields) > 8 else "",
        "address":      fields[11].replace("^", ", ").strip(", ") if len(fields) > 11 else "",
        "phone":        fields[13] if len(fields) > 13 else "",
    }
    return patient

def parse_obx(obx_segment):
    """Extract observation data from OBX segment."""
    fields = obx_segment.split("|")
    observation = {
        "set_id":        fields[1] if len(fields) > 1 else "",
        "value_type":    fields[2] if len(fields) > 2 else "",   # NM=Numeric, ST=String, CWE=Coded
        "loinc_code":    fields[3].split("^")[0] if len(fields) > 3 else "",
        "display_name":  fields[3].split("^")[1] if len(fields) > 3 and len(fields[3].split("^")) > 1 else "",
        "value":         fields[5] if len(fields) > 5 else "",
        "unit":          fields[6] if len(fields) > 6 else "",
        "reference_range": fields[7] if len(fields) > 7 else "",
        "status":        fields[11] if len(fields) > 11 else "",  # F=Final, P=Preliminary
        "observation_time": fields[14] if len(fields) > 14 else "",
    }
    return observation

def main():
    print("=" * 60)
    print("HealthBridge AI — Module 1: HL7 v2 Parser")
    print("=" * 60)

    # Split message into segments
    segments = SAMPLE_HL7.strip().split("\r")

    patient = None
    observations = []

    for seg in segments:
        seg_type = seg[:3]
        if seg_type == "PID":
            patient = parse_pid(seg)
        elif seg_type == "OBX":
            observations.append(parse_obx(seg))

    # ── Print Patient Info ───────────────────────────────────────────────────
    if patient:
        print("\n📋 PATIENT")
        print(f"  ID         : {patient['patient_id']}")
        print(f"  Name       : {patient['first_name']} {patient['last_name']}")
        print(f"  DOB        : {patient['date_of_birth']}")
        print(f"  Gender     : {patient['gender']}")
        print(f"  Address    : {patient['address']}")
        print(f"  Phone      : {patient['phone']}")

    # ── Print Observations ───────────────────────────────────────────────────
    print(f"\n🔬 OBSERVATIONS ({len(observations)} found)")
    print("-" * 60)
    for obs in observations:
        status_label = "Final" if obs["status"] == "F" else obs["status"]
        print(f"  [{obs['set_id']}] {obs['display_name']}")
        print(f"      LOINC       : {obs['loinc_code']}")
        print(f"      Value       : {obs['value']} {obs['unit']}")
        print(f"      Ref Range   : {obs['reference_range']}")
        print(f"      Status      : {status_label}")
        print(f"      Value Type  : {obs['value_type']}")
        print()

    print("=" * 60)
    print(f"✅ Parsed {len(observations)} OBX segments successfully.")
    print("   Next step: map these observations to FHIR R4 Observation JSON")
    print("=" * 60)

if __name__ == "__main__":
    main()
