import binascii
from Crypto.Cipher import AES

def decrypt_payload(cipher_file_path: str) -> str:
    """
    Reads the cipher text from cipher_file_path, executes AES-128-ECB
    decryption using the identified key, strips padding, and returns the flag.
    """
    # 1. Read hexadecimal ciphertext from file
    with open(cipher_file_path, "r") as f:
        hex_cipher = f.read().strip()
    
    # 2. Convert hex string to raw bytes
    ciphertext_bytes = binascii.unhexlify(hex_cipher)
    
    # TODO: Define the 16-byte key identified from the ECB pattern vulnerability
    key = b"K3Y!K3Y!K3Y!K3Y!"
    
    # TODO: Instantiate AES cipher in ECB mode
    cipher = AES.new(key, AES.MODE_ECB)
    
    # TODO: Decrypt payload and handle PKCS#7 or zero padding
    plaintext_bytes = cipher.decrypt(ciphertext_bytes)
    
    # Extract flag string from decrypted text
    decrypted_str = plaintext_bytes.decode('utf-8', errors='ignore')
    
    # Return string matching 'FLAG{...}'
    return decrypted_str.strip()


if __name__ == "__main__":
    # Local test execution
    print("Decrypted Output:", decrypt_payload("cipher.txt"))
