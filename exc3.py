r = int(input('enter a number'))
sum = 0
for num in range (1,r+1,1):
    sum += num
    print("sum of the number" , r , "is:" , sum)


class cat:
   def __init__(self, name, age):
     self.name = name
     self.age = age
   def sound(self):
       print("meow")
   def displayinfo(self):
        print(f'name: {self.name}')
        print(f'age:{self.age}')

class DomesticCat(cat):
    def __init__(self, name, age, owner, homeaddress):
        super().__init__(name, age)
        self.owner = owner
        self.homeaddress = homeaddress

cat1 = cat("Doud",5)
cat1.sound()
cat1.displayinfo()



bili = cat("gurmukh", 5)
print(bili)


