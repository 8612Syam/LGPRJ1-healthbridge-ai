import unittest
import json
import sys
import os

# This adds the current directory to the path so it can find fhir_mapper
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from fhir_mapper import map_obx_to_fhir

class TestFHIRMapping(unittest.TestCase):
    def setUp(self):
        self.sample_obx = {
            "name": "Glucose",
            "loinc": "2345-7",
            "value": "95",
            "units": "mg/dL",
            "status": "Final"
        }

    def test_loinc_mapping(self):
        fhir_json = json.loads(map_obx_to_fhir(self.sample_obx))
        loinc = fhir_json['code']['coding'][0]['code']
        self.assertEqual(loinc, "2345-7")

    def test_value_mapping(self):
        fhir_json = json.loads(map_obx_to_fhir(self.sample_obx))
        value = fhir_json['valueQuantity']['value']
        self.assertEqual(value, 95.0)

    def test_status_mapping(self):
        fhir_json = json.loads(map_obx_to_fhir(self.sample_obx))
        self.assertEqual(fhir_json['status'], "final")

if __name__ == "__main__":
    unittest.main()