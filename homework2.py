class Person:
    def __init__(self,name,birth_date,occupation,higher_education ):
        self.name = name
        self.birth_date = birth_date
        self.occupation = occupation
        self.higher_education = higher_education


    def introduce(self):
        if not self.higher_education:
            print(
                f'меня зовут {self.name} ,год моего рождения {self.birth_date}, по профессии {self.occupation}, высшего образования нет')
        else:
            print(
                f'меня зовут {self.name} ,год моего рождения {self.birth_date}, по профессии {self.occupation}, имеется высшее образование')

class Classmate(Person):
    def __init__(self,name,birth_date,occupation,higher_education,group_name):
        super().__init__(name,birth_date,occupation,higher_education)
        self.group_name = group_name

    def introduce(self):
      if not self.higher_education:
        print(
            f'I am Amina s groupmate, from {self.group_name} меня зовут {self.name} ,год моего рождения {self.birth_date}, по профессии {self.occupation}, высшего образования нет')
      else:
        print(
            f'I am Amina s groupmate, from {self.group_name}меня зовут {self.name} ,год моего рождения {self.birth_date}, по профессии {self.occupation}, имеется высшее образование')


class Friends(Person):
    def __init__(self,name,birth_date,occupation,higher_education, hobby):
        super().__init__(name,birth_date,occupation,higher_education)
        self.hobby = hobby

    def introduce(self):
         if not self.higher_education:
            print(
                    f'Hello  ,меня зовут {self.name} ,год моего рождения {self.birth_date}, по профессии {self.occupation}, высшего образования нет, a my hobby is {self.hobby}')
         else:
             print(
                    f'Hello, меня зовут {self.name} ,год моего рождения {self.birth_date}, по профессии {self.occupation}, имеется высшее образование ,a my hobby is {self.hobby}')



classmate1 = Classmate('ali',2008,'frontend',False,'asd12')
classmate2 = Classmate('Aliya',2007,'backend',True,'asd12')
friend1 = Friends('Aigul','2000','backend developer',True,'cooking')
friend2 = Friends('Alina','2001','data scientist',False,'play guitar')
classmate1.introduce()
classmate2.introduce()
friend1.introduce()
friend2.introduce()

#dop zadanie
people = [classmate1,classmate2,friend1,friend2]
for per in people:
    per.introduce()








