n = 21971
e = 131

message = "Hello world!"
encrypted_message = ""

############Encryption###########
for x in message:
    numerize = ord(x)
    encrypt = pow(numerize, e, n)
    denumerize = unichr(encrypt)
    encrypted message += denumerize
    
print encrypted_message