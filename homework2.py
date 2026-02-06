class Person:
    def __init__(self,name,birth_date,occupation,higher_education ):
        self.name = name
        self.birth_date = birth_date
        self.occupation = occupation
        self.higher_education = higher_education



    def introduce(self):
        if self.higher_education == False:
            print(
                f'меня зовут {self.name} ,год моего рождения {self.birth_date}, по профессии {self.occupation}, высшего образования нет')
        else:
            print(
                f'меня зовут {self.name} ,год моего рождения {self.birth_date}, по профессии {self.occupation}, имеется высшее образование')

class Classmate(Person):
    def __init__super(self,name,birth_date,group_name):
        self.group_name = group_name

    def introduce(self):
       print(f'my name is {self.name} , i born in {self.birth_date}, im in {self.group_name}')


class Friends(Person):
    def __init__super(self,name,birth_date,group_name,hobby):
        self.name = name
        self.birth_date = birth_date







