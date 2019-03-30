__author__ = '@Rishi @Pratham'

import unittest
from aes import AES
Test = 0 #Initialized the testing text variable

class AES_TEST(unittest.TestCase):
    def setUp(self):
        master_key = 0x2b7e151628aed2a6abf7158809cf4f3c
        self.AES = AES(master_key)

    def test_decryption(self):
        global plaintext
        ciphertext = self.AES.encrypt(plaintext)
        decrypted = self.AES.decrypt(ciphertext)
        self.assertEqual(plaintext)

if __name__ == '__main__':
    Text = int(input().encode('utf-8').hex()) #Taken the input
    unittest.main()
