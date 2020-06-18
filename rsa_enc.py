from Crypto.Signature import pkcs1_15
from Crypto.Hash import SHA256
from Crypto.PublicKey import RSA

# message = b'To be signed'
message = input("User-input message: ")
message_byte = bytes(message, 'utf-8')

key = RSA.import_key(open('private_key.txt').read())
h = SHA256.new(message_byte)
signature = pkcs1_15.new(key).sign(h)

# f_out = open("sigtext.txt", "wb")
# f_out.write(message)

f_out = open("sigtext.txt", "w")
f_out.write('{0} {1}\n'.format(message, signature))
f_out.close()