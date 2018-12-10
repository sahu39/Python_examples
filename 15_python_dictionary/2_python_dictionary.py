# Creating Dictionary & adding components#
def main():
    my_dict = {}
    my_dict_1 = {1:'john',2:'mayank'}
    my_dict_2 = dict({1:'sunil','name':'swagat'})
    my_dict_3 = dict([(1,'apple'),(2,'ball')])

    print(my_dict_1[1])
    print(my_dict_2['name'])
    print(my_dict_3[2])
    my_dict_2['address'] = 'Berhampur'
    print("my_dict_2:",my_dict_2)

if __name__ == "__main__":
    main()
