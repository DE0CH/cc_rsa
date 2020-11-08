from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
import base64


def new_private_key():
    private_key = RSA.generate(1024)
    return base64.urlsafe_b64encode(private_key.exportKey(format='DER')).decode('ascii')


def get_public_key(private_key):
    private_key = RSA.importKey(base64.urlsafe_b64decode(private_key))
    return base64.urlsafe_b64encode(private_key.publickey().exportKey(format='DER')).decode('ascii')


def encrypt_message(message, public_key):
    public_key = RSA.importKey(base64.urlsafe_b64decode(public_key))
    cipher = PKCS1_OAEP.new(public_key)
    cipher_text = cipher.encrypt(message.encode('utf-8'))
    cipher_text_64 = base64.urlsafe_b64encode(cipher_text).decode('ascii')
    return cipher_text_64


def decrypt_message(cipher_text, private_key):
    private_key = RSA.importKey(base64.urlsafe_b64decode(private_key))
    cipher = PKCS1_OAEP.new(private_key)
    cipher_text = base64.urlsafe_b64decode(cipher_text)
    return cipher.decrypt(cipher_text).decode('utf-8')

