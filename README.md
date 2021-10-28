# Simple Reverse Shell Generator

## :lock: Basic Information

**SimpleCrypt** is a simple python console application which provides encryption and decryption of files using the principles of an *asymmetric cryptography*.

> Asymmetric cryptography (Public-key cryptography), is a cryptographic system that uses pairs of keys. Each pair consists of a public key and a private key. Effective security requires keeping the private key private; the public key can be openly distributed without compromising security. In such a system, any person can encrypt a message using the intended receiver's public key, but that encrypted message can only be decrypted with the receiver's private key. An asymmetric key encryption scheme can be seen below.

<p align="center">
<img src="https://github.com/martinkubecka/SimpleCrypt/blob/main/images/public_key_cryptography.png" alt="Public Key Cryptography">
</p>

---
## :toolbox: Pre-requisites

Before running **SimpleCrypt** for the first time, you must have installed Python version 3.X, as well as the *PyCryptodome* package which can be installed with the following command:

```cmd
pip install pycryptodomex
```

---
## :desktop_computer: Usage

The application does not need to be compiled. If you have the python correctly set in the PATH variable, **SimpleCrypt** can be easily run from the operating system console or using the already compiled simplecrypt.exe.

### Encryption

<p align="center">
<img src="https://github.com/martinkubecka/SimpleCrypt/blob/main/images/enc.png" alt="Encryption">
</p>

### Decryption

<p align="center">
<img src="https://github.com/martinkubecka/SimpleCrypt/blob/main/images/dec.png" alt="Decryption">
</p>

### Generate RSA Key Pair

<p align="center">
<img src="https://github.com/martinkubecka/SimpleCrypt/blob/main/images/key_pair_gen.png" alt="Generate RSA Key Pair">
</p>

---
## :open_file_folder: Resources

- PyCryptodome’s documentation ([link](https://pycryptodome.readthedocs.io/en/latest/))
