from Crypto.Signature import pkcs1_15
from Crypto.Hash import SHA256
from Crypto.PublicKey import RSA

f_in = open("sigtext.txt", 'r')
message = f_in.read(18)
print(message)

message_byte = bytes(message,"utf-8")
# print("This really works")

signature = f_in.read()
print(signature)

f_in.close()

key = RSA.import_key(open('public_key.txt').read())
h = SHA256.new(message_byte)

try:
    pkcs1_15.new(key).verify(h, signature)
    print("The signature is valid.")
except (ValueError, TypeError):
    print("The signature is not valid.")