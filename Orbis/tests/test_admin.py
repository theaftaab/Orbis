import unittest

from fastapi.testclient import TestClient
from app import app

client = TestClient(app)


class TestAdminEndpoints(unittest.TestCase):
    def test_health_check(self):
        response = client.get(f"/admin/health-check", headers={"X-API-Key": "12345678-unsafe-master-key"})
        self.assertEqual(200, response.status_code)

    def test_generate_api_key(self):
        payload = {
            "scopes": ["sdk:true"]
        }
        response = client.post(f"/admin/generate-api-key",
                               headers={"X-API-Key": "12345678-unsafe-master-key", "Content-Type": "application/json"},
                               json=payload)
        self.assertEqual(200, response.status_code)
        self.assertIn("uid", response.json())
        self.assertIn("key", response.json())
        self.assertIn("scopes", response.json())
        return response.json()

    def test_revoke_api_key(self):
        r1 = self.test_generate_api_key()
        response = client.delete(f"/admin/revoke-api-key/{r1['uid']}",
                                 headers={"X-API-Key": "12345678-unsafe-master-key"})
        self.assertEqual(200, response.status_code)


if __name__ == '__main__':
    unittest.main()
