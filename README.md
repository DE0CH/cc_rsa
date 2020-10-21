# Simplified RSA Project

This project simplifies the RSA encryption by making a library in which methods easier to use at the expense of efficiency and flexibility
while keeping the principle of RSA intact.
It is good for educational purposes to showcase the RSA algorithm. To the best of the authors knowledge, this library is 
 cryptographically strong, but he takes no responsibility in any loss as a result of using this library and provides no warrenty.

## Installation
Note: As of October 21, 2020, the dependency of this project `pycrypto` does not support Python version higher than 3.7. 
So please use Python 3.7 or below. 

Clone the project and install the dependencies.
```
pip install -r requirements
```

## Documentation
There are only four methods in this library. In order to simplify the library, all is are represented with `String`.
1. `new_private_key()`. Returns a new private RSA private key.
2. `get_public_key(private_key)`. Takes the private key and returns the public key.
3. `encrypt_message(message, public_key)`. Takes the message and public key and return a cipher text.
4. `decrypt_meesage(cipher_text, private_key)`. Takes the cipher text and private key and returns the cipher text.

##Examples

Basic example:
```python
import cc_rsa
# Generate the key pair
private_key = cc_rsa.new_private_key()
public_key = cc_rsa.get_public_key(private_key)
message = 'my password is 12345'
# Encrypt the message
cipher_text = cc_rsa.encrypt_message(message, public_key)
# Decrypt the message
decrypted_message = cc_rsa.decrypt_message(cipher_text, private_key)
```

See `main.py` for a more elaborate example.