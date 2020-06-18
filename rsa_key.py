from Crypto.PublicKey import RSA
from Crypto.Random import get_random_bytes
from Crypto.Cipher import AES, PKCS1_OAEP

# generate RSA key
key = RSA.generate(2048)
private_key = key.export_key()

# open privateKey.txt
f_out = open("private_key.txt", "wb")
f_out.write(private_key) #write private_key key to private_key.pem

# export public key
public_key = key.publickey().export_key()
f_out = open("public_key.txt", "wb")
f_out.write(public_key) # write public key