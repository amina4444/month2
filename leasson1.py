class Car:
    def __init__(self,color,model):
        self.color = color
        self.model = model
        self.fined = False

    def drive_to(self,destination):
        if not self.fined:
         print('car driving to', destination)
        else:
            print('car on fine zone')

car_subaru = Car('silver','forester')
car_honda = Car('red','accord')

print(car_subaru)
car_subaru.drive_to('Bishkek')
print(car_honda)
print('Subaru: ',car_subaru.color, car_subaru.model)
print('Honda : ',car_honda.color, car_honda.model)

