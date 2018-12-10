#Python list extend() method #
def main():
    thelist=[1,"item",2,"jii"]
    alist=[3,6,8,"ri"]
    print("Before extending:"+str(thelist))
    thelist.extend(alist)
    print("After extending ",thelist)

if __name__ == "__main__":
    main()
