# ...
# Age less than 5 = frozenset
# under 18 / student = 15
# member = 20
# public = 300
# ...
# import random

# def calculate_ticket_price(category):
#     price = {
#         'young': 0,
#         'student':15
#         'member': 20,
#             'public':30
#     }
# chosen_category = price.get(category)
# retu


class person:
    def _init_(self, name, age, haircolor, eyecolor, hasbeard):
        self.name = name
        self.age = age
        self.haircolor = haircolor
        self.eyecolor = eyecolor
        self.hasbeard = hasbeard
 
# method
    def speaks(self):
      quote = input(f"what does {self.name} say?:")
      print(f"{self.name} says: ", quote)

#method with a parameter (years)
    def gets_older(self, year):
       self.age += year
       print(f"{self.name} is now {self.age}")

    def ishairy(self):
       if self.hasbeard == True:
        print(f"{self.name} has a cool beard.")
       else:
        print(f" {self.name} has a cool chain.")

cindy = person("cindy shaw", 45, "blonde", "brown")
henry = person("henry", 34, "brown", "blue")
cindy.speaks()
henry.gets_older(6)
cindy.ishairy()


cindy = person("cindy shaw", 45, "blonde", "brown")
henry = person("henry", 34, "brown", "blue")

print(cindy.name)
print(henry.age) 