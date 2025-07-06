# Decompiled with PyLingual (https://pylingual.io)
# Internal filename: chall.py
# Bytecode version: 3.11a7e (3495)
# Source timestamp: 1970-01-01 00:00:00 UTC (0)

from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
from Crypto.Random import get_random_bytes
import argparse

def encrypt_file(file):
    with open(file, 'rb') as f:
        data = f.read()
        f.close()
    key = get_random_bytes(16)
    #iv = get_random_bytes(8)
    cipher = AES.new(key, AES.MODE_CBC)
    print(key)
    print(cipher.iv)
    print(AES.block_size)
    encrypted = cipher.encrypt(pad(data, AES.block_size))
    outfile = file + ".enc"
    with open(outfile, 'wb') as f:
        f.write(encrypted)
        f.close()

def main():
    parser = argparse.ArgumentParser(description='Encrypt / decrypt file.')
    parser.add_argument('--encrypt', metavar='FILE', help='Specify the file to encrypt')
    parser.add_argument('--decrypt', metavar='ENCRYPTED_FILE', help='Specify the file to decrypt')
    args = parser.parse_args()
    if args.encrypt and args.decrypt:
        parser.error('You can only specify one action: --encrypt or --decrypt.')
    elif args.encrypt:
        print(f'Encrypting the file: {args.encrypt}')
        encrypt_file(args.encrypt)
        print('File encrypted')
    elif args.decrypt:
        print('Pay up at 15KK3cxwsk9igvHDCGnGtAc6ksNGKXcdsD to recover key for decryption')
    else:
        parser.error('You must specify either --encrypt or --decrypt.')
if __name__ == '__main__':
    main()