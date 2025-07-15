from Crypto.Cipher import Blowfish
from Crypto.Random import get_random_bytes

# Key generation
key = get_random_bytes(16)  # 16 bytes (128 bits) key

# Initialize the Blowfish cipher
cipher = Blowfish.new(key, Blowfish.MODE_ECB)

# Message to be encrypted
message = "Hello, Blowfish!"

# Padding the message to a multiple of 8 bytes
block_size = 8
padding = b"\0" * (block_size - len(message) % block_size)
message += padding

# Encrypt the message
ciphertext = cipher.encrypt(message.encode('utf-8'))

# Decrypt the message
decipher = Blowfish.new(key, Blowfish.MODE_ECB)
plaintext = decipher.decrypt(ciphertext).rstrip(padding).decode('utf-8')

print("Original Message:", message)
print("Encrypted:", ciphertext)
print("Decrypted Message:", plaintext)
