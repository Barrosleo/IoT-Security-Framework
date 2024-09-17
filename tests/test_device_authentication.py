import unittest
from device_authentication import generate_device_token, authenticate_device

class TestDeviceAuthentication(unittest.TestCase):
    def test_generate_device_token(self):
        device_id = 'device123'
        secret_key = 'supersecretkey'
        token = generate_device_token(device_id, secret_key)
        self.assertIsNotNone(token)

    def test_authenticate_device(self):
        device_id = 'device123'
        secret_key = 'supersecretkey'
        token = generate_device_token(device_id, secret_key)
        is_authenticated = authenticate_device(device_id, token, secret_key)
        self.assertTrue(is_authenticated)

if __name__ == '__main__':
    unittest.main()
