#regular expression to find out phone number#
#1st:import re module #
import re
def main():
#    print(isphonenumber('444-459-1256'))
#    Foundnumber = False
    message = 'My phone number is 415-435-5678 & my office number is 456-345-1231'
#2nd:Create regular expression object#
    regexobject = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
#3rd:Call the regexobject search() method to create a match object#
    matchedobj = regexobject.search(message)
    matchedobj2 = regexobject.findall(message)
#4th:Call the matchedobj group() method to get the 1st occurance of  matched string#
#----------------------------------------or---------------------------------------#
#4th:Call the matchedobj findall() method to return a list of strings of all ocuurance of found object#
    matchedstring = matchedobj.group()
#    matchedstringlist = matchedobj2.group()
    print(matchedstring)
    print(matchedobj2)    

if __name__ == '__main__':
    main()


    

