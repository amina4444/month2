class Animal:
    def __init__(self, name,age):
        self.__name = name
        self.__age = age

    def get_name(self):
            return self.__name

    def set_name(self, value):
            self.__name = value

    def get_age(self):
        return self.__age

    def set_age(self, value):
        self.__age = value

    def make_sound(self):
            print('sound')

class Dog(Animal):
    def __init__(self,name,age):
        super().__init__(name,age)


    def make_sound(self):
        print('gav')


class Cat(Animal):
    def __init__(self,name,age):
        super().__init__(name,age)

    def make_sound(self):
        print('mew')


dog = Dog('bobik',2)
print(f'name:{dog.get_name()}, age: {dog.get_age()}')
dog.make_sound()
dog.set_name('Snoop')
dog.set_age(6)
print(f' new name:{dog.get_name()}, new  age: {dog.get_age()}')

cat = Cat('pushok',1)
print(f'name: {cat.get_name()}, age {cat.get_age()}')
cat.make_sound()
cat.set_name('Maki')
cat.set_age(3)
print(f' new name: {cat.get_name()},  new age {cat.get_age()}')

