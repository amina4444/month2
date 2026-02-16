class Distance:
    conversion_dict = {
        'kilometers':1,'meters':0.01,'santimeters': 0.001
    }

    # метод для конвертации(преобразования) едини
    def convert(self):
        return self.value * Distance.conversion_dict.get(self.unit, 1)
    def __init__(self,value,unit):
        self.value = value
        self.unit = unit

    def __str__(self):
        return f'Distance: {self.value} {self.unit}'

    def __add__(self,other):
        sum = Distance((self.value,self.unit) + (other.value,other.unit))
        return sum
    def __sub__(self,other):
        sub = Distance((self.value,self.unit) + (other.value,other.unit))
        return sub

Dist = Distance(230,'meters')
Dist2 = Distance(99,'santimeters')
Dist3 = Distance(1,'kilometers')
print(Dist)
print(f'{Dist} + {Dist2} = {Dist.convert()+Dist2.convert()} km')
print(f'{Dist3} -  {Dist} = {Dist3.convert()-Dist.convert()} km')





