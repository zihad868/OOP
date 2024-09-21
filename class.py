class Person:
    def __init__(self, name):
        self.name = name;

    def sayHello(self):
        print('Hello.! i am ', self.name)

    def __del__(self):
        print( self.name, '-->', 'says bye.',)


person = Person('Jhon')
print("Name: ", person.name)
person.sayHello()
