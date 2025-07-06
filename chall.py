# Source Generated with Decompyle++
# File: chall.pyc (Python 3.11)

from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
from Crypto.Random import get_random_bytes
import argparse

def encrypt_file(file):
    pass
# WARNING: Decompyle incomplete


def main():
    parser = argparse.ArgumentParser(description = 'Encrypt / decrypt file.')
    parser.add_argument('--encrypt', metavar = 'FILE', help = 'Specify the file to encrypt')
    parser.add_argument('--decrypt', metavar = 'ENCRYPTED_FILE', help = 'Specify the file to decrypt')
    args = parser.parse_args()
    if args.encrypt and args.decrypt:
        parser.error('You can only specify one action: --encrypt or --decrypt.')
        return None
    if None.encrypt:
        print(f'''Encrypting the file: {args.encrypt}''')
        encrypt_file(args.encrypt)
        print('File encrypted')
        return None
    if None.decrypt:
        print('Pay up at 15KK3cxwsk9igvHDCGnGtAc6ksNGKXcdsD to recover key for decryption')
        return None
    None.error('You must specify either --encrypt or --decrypt.')

if __name__ == '__main__':
    main()
    return None
