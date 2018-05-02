#keys#
public_key = (21721, 113)
private_key = (21412, 14401)
encrypted_message = ("")
decrypted_message = ("")

message = 'Seven Nation Army'

e = ("")
n = ("")
d = ("")

#starting message#
def rsa():
    print ("Would you like to encrypt or decrypt?")
    print ("")
    print ("type 'e' to encrypt or 'd' to decrypt.")
    answer = input()
    if answer == 'e' or answer == 'E':
        print ("")
        print ("you chose to encrypt")
        print ("")
        encrypt(e,n)
        
    elif answer == 'd' or answer == 'D':
        print ("")
        print ("you chose to decrypt")
        print ("")
        decrypt(d,n)
    else:
        print ("")
        print ("answer not found, try again")
        rsa()
  
#encryption function#

def encrypt(e,n):
	print ("to encrypt please give the following:")
 	e = input("enter 'e' value: ")
	n = input("enter 'n' value: ")   
	print ("") 
	print ("enter the message you would like to encrypt")
 
answer = input()

for answer in input():
 numerize = ord(answer)
 encrypt = pow(numerize, e, n)
 denumerize = chr(encrypt)
 encrypted_message += denumerize

print encrypted_message

###decryption funcation###
def decrypt(d, n):
  encrypted_message = ''
  decrypted_message = ''
  message = input('What would you like to decrypt?')
  for t in message:
    numerize = ord(t)
    decrypt = pow(numerize, d, n)
    denumerize = chr(decrypt)
    decrypted_message += denumerize
  print(decrypted_message)
  #########
rsa()