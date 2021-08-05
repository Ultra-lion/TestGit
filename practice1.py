

x = "Global Variable"

def somefunc():
    global x #you g=have to specify it as global
    #because the value x = "variable x" is only defined in the local scope of function
    #and won't have any effect in to the global variable unless specified
    x = 'variable x'
    def innerfunc():
        print(x)
    innerfunc()
    # print(x)


def somechangefunc(list):
    list = list.append("2")


if __name__ == '__main__':

    # x = "main variable"
    print(x)

    # somefunc()

    # list = ["1"]
    # print(x)
    # str = "1 "
    # somechangefunc(list)
    # print(list)
