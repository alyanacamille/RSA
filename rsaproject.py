
#starting message#
def rsa():
    print "Would you like to encrypt or decrypt?"
    print ""
    print "type 'e' to encrypt or 'd' to decrypt."
    answer = raw_input()
    if answer == 'e' or answer == 'E':
        print ""
        print "you chose to encrypt"
        print ""
        encrypt()
    elif answer == 'd' or answer == 'D':
        print ""
        print "you chose to decrypt"
        print ""
        #decrypt function
    else:
        print ""
        print "answer not found, try again"
        rsa()
  
#encryption function#      
def encrypt():
    print "to encrypt please give the following:"
    e = input("enter 'e' value: ")
    n = input("enter 'n' value: ")    
    print "enter the message you would like to encrypt:"
    answer = raw_input()


###
rsa()