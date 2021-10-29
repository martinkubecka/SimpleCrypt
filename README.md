# SimpleCrypt

## :lock: Basic Information

**SimpleCrypt** is a python console application which provides authenticated encryption and decryption of files using the principles of an *asymmetric cryptography*.

> Asymmetric cryptography (Public-key cryptography), is a cryptographic system that uses pairs of keys. Each pair consists of a public key and a private key. Effective security requires keeping the private key private; the public key can be openly distributed without compromising security. In such a system, any person can encrypt a message using the intended receiver's public key, but that encrypted message can only be decrypted with the receiver's private key. An asymmetric key encryption scheme can be seen below.

</br>

<p align="center">
<img src="https://github.com/martinkubecka/SimpleCrypt/blob/main/images/public_key_cryptography.png" alt="Public Key Cryptography">
</p>

</br>

Encryption and decryption uses **AES** (Advanced Encryption Standard) block cipher with **GCM** (Galois / Counter) block cipher mode. GCM mode is an authenticated encryption algorithm designed to provide both data authenticity (integrity) and confidentiality. The randomly generated symmetric key with which we encrypt the given file is encrypted with the provided (recipient's) 2048-bit public key and then saved in the header of the ouput file. In our implementation, we chose to write the **MAC** integrity tag also at the beginning of the output file in its header.

In the image below we can see the structure of the output (encrypted) file.

</br>

<p align="center">
<img src="https://github.com/martinkubecka/SimpleCrypt/blob/main/images/file_structure.png" alt="Output File Structure">
</p>


---
## :toolbox: Pre-requisites

Before running **SimpleCrypt** for the first time, you must have installed Python version 3.X, as well as the *PyCryptodome* package which can be installed with the following command:

```
pip install pycryptodomex
```

---
## :desktop_computer: Usage

The application does not need to be compiled. If you have the python correctly set in the PATH variable, **SimpleCrypt** can be easily run from the operating system console or using the already compiled simplecrypt.exe.

### Encryption

- Choose option **E**.
- Enter file location (absolute path if the file is not in the current working directory).
- Provide recipient's public key location (absolute path if the file is not in the current working directory).
- New encryptd file will be created inside the current working directory.

```
PS E:\Programming\SimpleCrypt> python .\simplecrypt.py

       _____            __    _____              __
      / __(_)_ _  ___  / /__ / ___/_____ _____  / /_
     _\ \/ /  ' \/ _ \/ / -_) /__/ __/ // / _ \/ __/
    /___/_/_/_/_/ .__/_/\__/\___/_/  \_, / .__/\__/
               /_/                  /___/_/

                            by Martin Kubecka, 2021
    ------------------------------------------------

[+] Choose one of the following options
1) Option G for RSA key pair generation
2) Option E for file encryption
3) Option D for file decryption
4) Option Q to exit

[+] Please enter your choice:
> E

[+] Enter file location:
> E:\Documents\The_X-Files.pdf

[+] Enter recipient's public key location:
> E:\Programming\SimpleCrypt\id_rsa.pub

Writing to the output file . . . . . . . .

Encrypting . . . . . . . . . . . . . . . .


[+] File successfully encrypted in 0.004003047943115234 seconds

Writing encrypted data to the file . . . .
Writing the MAC tag to the output file . .
```

### Decryption

- Choose option **D**.
- Enter file location (absolute path if the file is not in the current working directory).
- Provide your private key location (absolute path if the file is not in the current working directory).
	- This key is in the pair with the public key, which sender used to encrypt the file.
- New decrypted file will be created inside the current working directory.

```
PS E:\Programming\SimpleCrypt> python .\simplecrypt.py

       _____            __    _____              __
      / __(_)_ _  ___  / /__ / ___/_____ _____  / /_
     _\ \/ /  ' \/ _ \/ / -_) /__/ __/ // / _ \/ __/
    /___/_/_/_/_/ .__/_/\__/\___/_/  \_, / .__/\__/
               /_/                  /___/_/

                            by Martin Kubecka, 2021
    ------------------------------------------------

[+] Choose one of the following options
1) Option G for RSA key pair generation
2) Option E for file encryption
3) Option D for file decryption
4) Option Q to exit

[+] Please enter your choice:
> D

[+] Enter file location:
> E:\Documents\The_X-Files_encrypted.pdf

[+] Enter private key location:
> E:\Programming\SimpleCrypt\id_rsa

Reading the provided private key . . . . .
Reading the encrypted file . . . . . . . .

Decrypting . . . . . . . . . . . . . . . .


[+] File successfully decrypted in 0.004000186920166016 seconds

Verifying decrypted data . . . . . . . . .
Writing decrypted data to the file . . . .
```

### Generate RSA Key Pair

- Choose option **G**.
- RSA key pair will be generated in the current working directory.
	- Public key: `id_rsa.pub`
	- Private key: `id_rsa`

```
PS E:\Programming\SimpleCrypt> python .\simplecrypt.py

       _____            __    _____              __
      / __(_)_ _  ___  / /__ / ___/_____ _____  / /_
     _\ \/ /  ' \/ _ \/ / -_) /__/ __/ // / _ \/ __/
    /___/_/_/_/_/ .__/_/\__/\___/_/  \_, / .__/\__/
               /_/                  /___/_/

                            by Martin Kubecka, 2021
    ------------------------------------------------

[+] Choose one of the following options
1) Option G for RSA key pair generation
2) Option E for file encryption
3) Option D for file decryption
4) Option Q to exit

[+] Please enter your choice:
> G

Generating a public/private RSA key pair . . . . .
Successfully generated the public/private key pair
```

---
## :open_file_folder: Resources

- PyCryptodome’s documentation ([link](https://pycryptodome.readthedocs.io/en/latest/))
- PyCryptodome’s RSA documentation ([link](https://pycryptodome.readthedocs.io/en/latest/src/public_key/rsa.html))
