

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


class testclass():
    __instance = None
    def __init__(self,str):
        self.name1  = str

    def tellname(self):
        return self.name1

if __name__ == '__main__':

    # x = "main variable"
    # print(x)


    cls =testclass("Rohan")
    cls2 =testclass("Afnan")

    print(cls.__instance)
    print(cls2.tellname())
    # somefunc()

    # list = ["1"]
    # print(x)
    # str = "1 "
    # somechangefunc(list)
    # print(list)
