
# algorithm\test.py
import unittest
import random
import string

from algorithms.caesar import encrypt as caesar_encrypt, decrypt as caesar_decrypt
from algorithms.substitution import encrypt as encrypt_sub, decrypt as decrypt_sub
class Test(unittest.TestCase):

    def testcaesar(self):
        for i in range(60):
            message_length = random.randint(5,30)
            message = ''.join(
                random.choice(string.ascii_letters+".,!?"))
            for j in range(message_length):
                shift = random.randint(-100,100)
                encrypted = caesar_encrypt(message, shift)
                decrypted = caesar_decrypt(encrypted, shift)
                self.assertEqual(message,decrypted)
    def testsubstitution(self):
        for i in range(60):
             message_length=random.randint(5,30)
             message=''.join(
                 random.choice(string.ascii_lowercase+".,!?") 
             for j in range(message_length)
              )
             
             
             alphabet=list(string.ascii_lowercase) 
             random.shuffle(alphabet)
             key =''.join(alphabet)
             encrypted = encrypt_sub(message, key)
             decrypted = decrypt_sub(encrypted, key)
             self.assertEqual(message,decrypted)

if __name__=="__main__":
    unittest.main()             




                