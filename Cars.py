class Car:

  def __init__(self, year, make, model, num_doors, roof):
    self.year = year
    self.make = make
    self.model = model
    self.num_doors = num_doors
    self.roof = roof

  def give_intel(self):
    print(f" Your car's \nyear:{self.year}\n")
    print(f" Your car's \nmake:{self.make}\n")
    print(f" Your car's \nmodel:{self.model}\n")
    print(f"Your car's \nnumber of doors:{self.num_doors}\n")
    print(f"Your car's \nroof:{self.roof}\n")


class Vihicles(Car):

  def __init__(self, year, make, model, num_doors, roof, vehicle):
    super().__init__(year, make, model, num_doors, roof)
    self.vehicle = vehicle

  def give_intel(self):
    print(f" Your {self.vehicle}'s \nyear:{self.year}\n")
    print(f" Your {self.vehicle}'s \nmake:{self.make}\n")
    print(f" Your {self.vehicle}'s \nmodel:{self.model}\n")
    print(f"Your {self.vehicle}'s \n number of doors:{self.num_doors}\n")
    print(f"Your {self.vehicle}'s \nroof:{self.roof}\n")
    print(
        f"We charge more for our{self.vehicle}'s we're are in limmited supply of them "
    )


q = "none"
print("Welcome to the dealership! \nWhat vehicle would you like to purchase?")
q = input("type car if you want to buy a car---->").lower()
while q == "car":

  try:
    yr = int(input("year of your car-->"))
    mk = input("Make -->")
    md = input("Model -->")
    doors = int(input("amount of doors"))
    roof = input("Roof?")
    mycar = Car(yr, mk, md, doors, roof)
    mycar.give_intel()
    break

  except:
    print(
        "That is invalid information numbers only for the doors and the year; Try Again"
    )
    continue

while not q == "none" and not q == "car":
  try:
    yr = int(input(f"year of your {q}-->"))
    mk = input("Make -->")
    md = input("Model -->")
    doors = int(input("amount of doors"))
    roof = input("Roof?")
    myvehicle = Vihicles(yr, mk, md, doors, roof, q)
    myvehicle.give_intel()
    break

  except:
    print(
        "That is invalid information numbers only for the doors and the year; Try Again"
    )
    continue