#Without regular expression to find out phone number#
def isphonenumber(text):
    if len(text) != 12:
        return False  #Not phone number
    for i in range(0,3):
        if not text[i].isdecimal():
            return False #No area code
    if text[3] != '-':
        return False #missing dash
    for i in range(4,7):
        if not text[i].isdecimal():
            return False #no numbers
    if text[7] != '-':
        return False
    for i in range(8,11):
        if not text[i].isdecimal():
            return False
    return True
def main():
#    print(isphonenumber('444-459-1256'))
    Foundnumber = False
    message = 'My phone number is 415-435-5678 & my office number is 456-345-1231'
    for i in range(len(message)):
        chunk = message[i:i+12]
        if isphonenumber(chunk):
            print('Phone number found: '+chunk)
            Foundnumber = True
    if Foundnumber == False:
        print('No phone number is found')

if __name__ == '__main__':
    main()


    

