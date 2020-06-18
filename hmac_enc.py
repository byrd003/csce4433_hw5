from Crypto.Hash import HMAC, SHA256

m = input("User input message: ")
m_byte = bytes(m, "utf-8")

k = b'Swordfish'

h = HMAC.new(k, digestmod=SHA256)
h.update(m_byte)
print(h.hexdigest())


# h_bytes = bytes()

f_out = open("mactext.txt", "w")
f_out.write('{0} {1}\n'.format(m, h.hexdigest()))
f_out.close()