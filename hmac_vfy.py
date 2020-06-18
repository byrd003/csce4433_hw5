from Crypto.Hash import HMAC, SHA256

 # We have received a message 'msg' together
 # with its MAC 'mac'

f_in = open("mactext.txt", 'r')

m = f_in.read(16)
m_bytes = bytes(m, "utf-8")
print(m)

# print("this works")

hr = f_in.read()
hr_bytes = bytes(hr, "utf-8")
print(hr)

f_in.close()

# msg = b"Hello World"
k = b'Swordfish'



# message_byte = bytes(message,"utf-8")
# print("This really works")

# signature = f_in.read()
# print(signature)

h= HMAC.new(m_bytes, digestmod=SHA256)
# h.update(m_bytes)

try:
    h.hexverify(hr)
    print("The message is authentic")
except ValueError:
    print("The message or the key is wrong")