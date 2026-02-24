class Person:
    def __init__(self,name,birth_date,occupation,higher_education ):
        self.name = name
        self.birth_date = birth_date
        self.__occupation = occupation
        self.__higher_education = higher_education
    @property
    def occupation(self):
        return self.__occupation

    @property
    def higher_education(self):
        return self.__higher_education

    def introduce(self):
        if not self.__higher_education:

            print(
                f'меня зовут {self.name} ,год моего рождения {self.birth_date}, по профессии {self.__occupation}, высшего образования нет')
        else:
            print(
                f'меня зовут {self.name} ,год моего рождения {self.birth_date}, по профессии {self.__occupation}, имеется высшее образование')
            return

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



class Friend(Person):
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
friend1 = Friend('Aigul','2000','backend developer',True,'cooking')
friend2 = Friend('Alina','2001','data scientist',False,'play guitar')
classmate1.introduce()
classmate2.introduce()
friend1.introduce()
friend2.introduce()