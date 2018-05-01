#decryption funcation#
encrypted_message = '⫾䖩仪㉘ಊ㰘呈䐚冓⫾䖩ວ㉘ಊ㰘呈䐚冓'

e = 113
d = 1441

    
def decryption(d, n):
  message = input
  encrypted_message = ''
  decrypted_message = ''
  message = input ('What would you like to decrypt?')
  
for t in message(input):
   numerize = ord(t)
   decrypt = pow(numerize, d, n)
   denumerize = chr(decrypt)
   decrypted_message += denumerize
    
print (decrypted_message)
      
      