class Person:
    def speak(self):
        print('I can speak')


class Man(Person):
    def wear(self):
        print('Wear shirt')


class Woman(Person):
    def wear(self):
        print('Wear skirt')


person = Person()
man = Man()

man.speak()
