import cc_rsa


def get_new_keys():
    print('Welcome to my secrete message sender')
    private_key = cc_rsa.new_private_key()
    print('Your private key is (don\'t show it to others):')
    print(private_key)
    print('Your public key is:')
    print(cc_rsa.get_public_key(private_key))


def encrypt_message():
    public_key = input('What is the public key?\n')
    message = input('What is the message?\n')
    print('Your encrypted message is:')
    print(cc_rsa.encrypt_message(message, public_key))


def decrypt_message():
    private_key = input('What is the private key?\n')
    code = input('What is the encrypted message?\n')
    print('The decoded message is:')
    print(cc_rsa.decrypt_message(code, private_key))


if __name__ == '__main__':
    get_new_keys()

