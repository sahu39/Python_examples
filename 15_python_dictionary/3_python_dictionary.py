# Dictionary fromkey() usages#
def main():
    #fromkey() usage1#
    keys = {1,2,3,"age"}
    my_dict = dict.fromkeys(keys)
    print('my_dict',my_dict)
    
    #fromkeys() usage2 #
    keys = {'key1','key2','key3'}
    values = {"sunil",26,"berhampur"}
    my_dict = dict.fromkeys(keys,values)
    print('my_dict:',my_dict)

if __name__ == "__main__":
    main()
