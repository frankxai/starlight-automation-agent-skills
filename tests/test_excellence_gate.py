"""Offline tests for the Starlight evidence gate."""
import unittest
from scripts.excellence_gate import validate

GOOD={"id":"mission-1","objective":"Build and test","role":"sol","owner":"starlight","source_revision":"abc123","authorized_effects":["draft branch"],"artifacts":["artifact-url"],"acceptance":{"unit_tests":True},"status":"tested","verification_receipts":["unit-test-log"],"scores":{"reasoning":9,"originality":9,"craft":9,"correctness":10,"completeness":9,"evidence":9}}

class EvidenceGateTests(unittest.TestCase):
    def test_valid_tested(self):self.assertTrue(validate(GOOD)["pass"])
    def test_missing_receipt(self):
        x={k:v for k,v in GOOD.items() if k!="verification_receipts"}
        self.assertIn("missing:verification_receipts",validate(x)["errors"])
    def test_failure_blocks(self):
        self.assertIn("failed:acceptance",validate({**GOOD,"acceptance":{"unit_tests":False}})["errors"])
    def test_deployed_requires_receipt(self):
        self.assertIn("missing:deployment_receipt",validate({**GOOD,"status":"deployed","reviewer":"verity"})["errors"])
    def test_low_quality_blocks(self):
        self.assertIn("failed:quality-threshold",validate({**GOOD,"scores":{**GOOD["scores"],"craft":3}})["errors"])
    def test_invalid_role(self):
        self.assertIn("invalid:role",validate({**GOOD,"role":"omnipotent"})["errors"])
    def test_implemented_not_fake_tested(self):
        self.assertTrue(validate({**GOOD,"status":"implemented","verification_receipts":[]})["pass"])

if __name__=="__main__":unittest.main()
