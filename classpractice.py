class Animal():
    what_am_i = "Animal"

    def __init__(self):
        print("Animal Created")

    def eat(self):
        print("Ate Food")

    def sleep(self):
        print("Slept")

    def __del__(self):
        print("Animal Destroyed")

class dog(Animal):
    def __init__(self):
        Animal.__init__(self)
        print("Dog Created")

    def __del__(self):
        print("Dog Destroyed")
if __name__ == '__main__':
    a = dog()
    # b = Animal()
