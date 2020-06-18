import timeit
import numpy as np
from Crypto.Util.Padding import pad, unpad
from base64 import b64encode, b64decode
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
from Crypto.Hash import HMAC, SHA256
from Crypto.Signature import pkcs1_15

def hmac_gen():
    m = input("User-input message for HMAC Generation: ")
    m_byte = bytes(m, 'utf-8')
    k = get_random_bytes(16)

    h = HMAC.new(k, digestmod=SHA256)
    # hmac_rep = (timeit.timeit('hmac = HMAC.new(k, digestmod=SHA256)',
	# 	globals={'HMAC':HMAC,'k':k,'SHA256':SHA256},number=100))

    hmac_rep = (timeit.timeit('h.update(m_byte)',
		globals={'h':h,'m_byte':m_byte},number=100))

    avg_hmac = np.mean(hmac_rep)
    print("Average HMAC generation time: ")
    print(avg_hmac)   

def signature():
    keyPair = RSA.generate(2048)
    pubKey = keyPair.publickey()
    pubKeyPEM = pubKey.exportKey()
    privKeyPEM = keyPair.exportKey()

    m = input("User-input message for RSA Digital Signature: ")
    m_byte = bytes(m, 'utf-8')

    key = RSA.import_key(open('private_key.txt').read())
    h = SHA256.new(m_byte)
    sig_gen_rep = (timeit.timeit('signature = pkcs1_15.new(key).sign(h)',
        globals={'signature':signature,'pkcs1_15':pkcs1_15,'key':key,'h':h},number = 100))
    avg_sig_gen = np.mean(sig_gen_rep)

    ver_sig = pkcs1_15.new(key).sign(h)
    sig_ver_rep = (timeit.timeit('pkcs1_15.new(key).verify(h, ver_sig)',
        globals={'pkcs1_15':pkcs1_15,'key':key,'h':h,'ver_sig':ver_sig},number = 100))
    avg_sig_ver = np.mean(sig_ver_rep)

    print("Average Signature generation time: ")
    print(avg_sig_gen)
    print("Average Signature verification time: ")
    print(avg_sig_ver)   


hmac_gen()
signature()
