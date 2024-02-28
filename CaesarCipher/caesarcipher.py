
def encrypt(plaintext, shift):
	ciphertext = ""

	for i in range(len(plaintext)):
		temp = plaintext[i].upper()

		if plaintext[i] != ' ':
			ciphertext += chr((ord(temp) + shift - 65) % 26 + 65)
		else:
			ciphertext += plaintext[i]

	return ciphertext

def decrypt(ciphertext, shift):
	plaintext = ""

	for i in range(len(ciphertext)):
		temp = ciphertext[i].upper()
		if ciphertext[i] != ' ':
			plaintext += chr((ord(temp) - shift - 65) % 26 + 65)
		else:
			plaintext += ciphertext[i]

	return plaintext

def bf_decrypt(ciphertext):
	for s in range(1,26):
		plaintext = ""
		for i in range(len(ciphertext)):
			temp = ciphertext[i].upper()
			if ciphertext[i] != ' ':
				plaintext += chr((ord(temp) - s - 65) % 26 + 65)
			else:
				plaintext += ciphertext[i]
		print("Shift Length: ", s, "   Decrypted message: ", plaintext)

input_message = "HELLO WORLD"
shift = 4

print("Input: ", input_message)
print("\nEncrypted message: ", encrypt(input_message, shift))
decrypt_message = encrypt(input_message, shift)
print("Decrypted message: ", decrypt(decrypt_message, shift))
bf_decrypt(decrypt_message)

