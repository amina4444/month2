class Person:
    def __init__(self,name,birth_date,occupation,higher_education ):
        self.name = name
        self.birth_date = birth_date
        self.occupation = occupation
        self.higher_education = higher_education

    def introduce(self):
        if self.higher_education == False:
         print(f'меня зовут {self.name} ,год моего рождения {self.birth_date}, по профессии {self.occupation}, высшего образования нет')
        else:
            print(f'меня зовут {self.name} ,год моего рождения {self.birth_date}, по профессии {self.occupation}, имеется высшее образование')


person1 = Person('Aigul','2000','backend developer',True)
person2 = Person('Alina','2001','data scientist',False)
person3 = Person('Dinara','1970','doctor',True)
print(person1.name , person1.birth_date , person1.occupation , person1.higher_education )
print(person2.name, person2.birth_date , person2.occupation , person2.higher_education)
print(person3.name,  person3.birth_date , person3.occupation , person3.higher_education)


person1.introduce()
person2.introduce()
person3.introduce()


