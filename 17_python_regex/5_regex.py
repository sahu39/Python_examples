#regex example#
import re
def main():
    #Create regex object#
    phonenumberregex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
    #search the string using search method#
    mo = phonenumberregex.search('My phone number is 321-456-4557')
    #use group nethod of matched object mo#
    phonenumber = mo.group()
    print(phonenumber)
    phoneareacode = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')
    areacodeobj = phoneareacode.search('My no is 123-456-4569')
    areacode = areacodeobj.group(1)
    print(areacode)
    

if __name__ == "__main__":
    main()
