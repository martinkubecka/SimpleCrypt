import os
import time
import sys
from Cryptodome.Cipher import AES, PKCS1_OAEP
from Cryptodome.PublicKey import RSA
from Cryptodome.Random import get_random_bytes


def key_pair_gen():
    # generate RSA (2048) public/private key pair
    private_key = RSA.generate(2048)
    public_key = private_key.publickey()

    print('\nGenerating a public/private RSA key pair . . . . . ')
    with open('id_rsa.pub', 'wb') as pb_key:
        pb_key.write(public_key.export_key())

    with open('id_rsa', 'wb') as pv_key:
        pv_key.write(private_key.export_key())

    print('Successfully generated the public/private key pair\n')


def encryption():
    print('\n[+] Enter file location: ')
    file_location = input('> ')
    filename, file_extension = os.path.splitext(file_location)

    # read and save data from provided file
    try:
        in_file = open(file_location, "rb")
        data = in_file.read()
        in_file.close()
    except FileNotFoundError as fnf_error:
        print('\n')
        sys.exit(fnf_error)

    print('\n[+] Enter recipient\'s public key location: ')
    pub_key_location = input('> ')

    # read recipient's public key
    try:
        key_in = open(pub_key_location, "rb")
        public_key = RSA.import_key(key_in.read())
        key_in.close()
    except FileNotFoundError as fnf_error:
        print('\n')
        sys.exit(fnf_error)

    # generate random 16 bytes key
    key = get_random_bytes(16)
    # encrypt the key with the public key
    key_cipher = PKCS1_OAEP.new(key=public_key)
    key_encrypted = key_cipher.encrypt(key)

    try:
        # create an encrypted AES cipher object with the key using the GCM mode
        cipher = AES.new(key, AES.MODE_GCM)
        nonce = cipher.nonce

        # set up the output file and write header to the output file
        output_file = filename + '_encrypted' + file_extension
        file_out = open(output_file, "wb")
        print('\nWriting to the output file . . . . . . . .')
        file_out.write(key_encrypted)
        file_out.write(nonce)
        file_out.write(get_random_bytes(16))

        print('\nEncrypting . . . . . . . . . . . . . . . .\n')
        start_time = time.time()
        ciphertext = cipher.encrypt(data)
        print("\n[+] File successfully encrypted in %s seconds\n" % (time.time() - start_time))

        # write encrypted data to the output file
        print('Writing encrypted data to the file . . . .')
        file_out.write(ciphertext)

        # create MAC tag and appended it at the of the header, right before ciphertext
        print('Writing the MAC tag to the output file . .\n')
        file_out.seek(272)  # 256 + 16 ; encrypted key + nonce
        tag = cipher.digest()
        file_out.write(tag)

        file_out.close()

    except ValueError:
        sys.exit('\n[!] There was an error while encrypting the file\n')


def decryption():
    print('\n[+] Enter file location: ')
    input_file = input('> ')
    filename, file_extension = os.path.splitext(input_file)
    file_name_orig = str(filename).replace('_encrypted', '')
    print('\n[+] Enter private key location: ')
    key_location = input('> ')

    # read and save data from the provided key file
    print('\nReading the provided private key . . . . .')
    try:
        key_in = open(key_location, 'rb')
        private_key = RSA.import_key(key_in.read())
        key_in.close()
    except FileNotFoundError as fnf_error:
        print('\n')
        sys.exit(fnf_error)

    key_cipher = PKCS1_OAEP.new(key=private_key)

    # read and save data from the provided encrypted file
    print('Reading the encrypted file . . . . . . . .')
    try:
        file_in = open(input_file, 'rb')
        key = key_cipher.decrypt(file_in.read(256))
        nonce = file_in.read(16)
        tag = file_in.read(16)
        ciphered_data = file_in.read()
        file_in.close()
    except FileNotFoundError as fnf_error:
        print('\n')
        sys.exit(fnf_error)

    try:
        # setup cipher and decrypt data
        cipher = AES.new(key, AES.MODE_GCM, nonce=nonce)

        print('\nDecrypting . . . . . . . . . . . . . . . .\n')
        start_time = time.time()
        original_data = cipher.decrypt(ciphered_data)
        print("\n[+] File successfully decrypted in %s seconds\n" % (time.time() - start_time))

        # check if the decrypted data is valid and it has not been tampered with
        print('Verifying decrypted data . . . . . . . . .')
        cipher.verify(tag)

    except ValueError as val_error:
        sys.exit('\n[!] There was an error while decrypting the file\n')

    # set up the output file and then write decrypted data inside
    try:
        print('Writing decrypted data to the file . . . .\n')
        output_file = file_name_orig + '_decrypted' + file_extension
        output_file = open(output_file, "wb")
        output_file.write(original_data)
        output_file.close()
    except AssertionError as error:
        sys.exit('\n[!] There was an error while writing to the output file\n')


def header():
    print(r"""
       _____            __    _____              __  
      / __(_)_ _  ___  / /__ / ___/_____ _____  / /_
     _\ \/ /  ' \/ _ \/ / -_) /__/ __/ // / _ \/ __/
    /___/_/_/_/_/ .__/_/\__/\___/_/  \_, / .__/\__/
               /_/                  /___/_/        

                            by Martin Kubecka, 2021
    ------------------------------------------------
    """)


def menu():
    print('[+] Choose one of the following options')
    print('1) Option G for RSA key pair generation')
    print('2) Option E for file encryption')
    print('3) Option D for file decryption')
    print('4) Option Q to exit')
    while 1:
        print('\n[+] Please enter your choice: ')
        option = input('> ')

        if (option == 'G') or (option == 'g'):
            key_pair_gen()
        elif (option == 'E') or (option == 'e'):
            encryption()
        elif (option == 'D') or (option == 'd'):
            decryption()
        elif (option == 'Q') or (option == 'q'):
            sys.exit('\nGoodbye\n')
        else:
            print('\n[!] INVALID INPUT\n')
        print('    ------------------------------------------------')


def main():
    header()
    menu()


if __name__ == '__main__':
    main()
