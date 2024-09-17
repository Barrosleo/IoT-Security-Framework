import unittest
from secure_communication import create_secure_socket

class TestSecureCommunication(unittest.TestCase):
    def test_create_secure_socket(self):
        host = 'example.com'
        port = 443
        secure_sock = create_secure_socket(host, port)
        self.assertIsNotNone(secure_sock)
        secure_sock.close()

if __name__ == '__main__':
    unittest.main()
