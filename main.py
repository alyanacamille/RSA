
#encrypt#
def encryption(e, n):
	encrypted_message = ""
	message = input("what would you like to encrypt: ")
	for x in message:
		numerize = ord(x)
		encrypt = pow(numerize, e, n)
		denumerize = chr(encrypt)
		encrypted_message += denumerize
	print(encrypted_message)
	print("")
	RSA()

#decrypt#
def decryption(d, n):
	decrypted_message = ""
	emessage = input("what would you like to decrypt: ")
	for t in emessage:
		numerize = ord(t)
		decrypt = pow(numerize, d, n)
		denumerize = chr(decrypt)
		decrypted_message += denumerize
	print(decrypted_message)
	print("")
	
def RSA():
	print("what would you like to do?")
	print("type 'encrypt' to encrypt a message")
	print("type 'decrypt' to decrypt a message")
	print("type 'leave' to leave")
	choice = input("your response: ")
	while input != choice:
		if choice == "encrypt":
			e = int(input("your 'e' # : "))
			n = int(input("your 'n' # : "))
			encryption(n, e)
		if choice == "decrypt":
			d = int(input("your 'd' # : "))
			PhiN = int(input("enter your 'n' # : "))
			decryption(d, PhiN)
		if choice == "leave":
			break
		else:
			RSA()
			break
			
	RSA()