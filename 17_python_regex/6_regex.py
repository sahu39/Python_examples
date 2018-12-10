#regex using pipe #
import re
def main():
    batregex = re.compile(r'Bat(man|mobile|copter|motor)')
    mo = batregex.search('I am Batman')
    exp = mo.group()
    print(exp)



if __name__ == "__main__":
    main()

