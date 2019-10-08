# testing out messages
print("hello world")
print("Howdy y'all")
print("I like typing this.")
print("This is fun.")

# trying out some maths with chickens
print("I will now count my chickens", 2)
print("Hens: ", 25+30/6)
print("Roosters: ", 100 - 25 * 3 % 4)

# trying out more maths with eggs.
print("Now i will count the eggs", 7)
print(3 + 2 + 1 - 5 + 4 % 2 - 1 / 4 + 6)
print(3 + 2< 5 - 7)

# make more math problems
print(5 + 3 + 2 - 5 % 6 / 6 + 8)
# fixing the math
print(5.0 + 3.3 + 2.0 - 5.0 % 6.7 / 6.0 + 8.0)

# variables and some of their powers
cars = 80
spaceInACar = 4.0
drivers = 45
passengers = 115
cars_not_driven = cars - drivers
cars_driven = drivers
carpool_capacity = spaceInACar * cars_driven
average_passengers_per_car = passengers / cars_driven

print("there are", cars, "cars available.")
print("there are only", drivers, "deivers available today.")
print("there will be", cars_not_driven, "empty cars today.")
print("we can transport", carpool_capacity, "people today")
print("we have", passengers, "to carpool today.")
print("we need to put approximately", average_passengers_per_car, "people in each car." )

# using variables in my story
seats = 460
row_of_seats = 23
audience = 340
empty_seats = seats - audience
seats = audience
average_row_capacity = seats / row_of_seats

print("there are", seats, "seats available.")
print("there are only", row_of_seats, "row of seats available today.")
print("there will be", empty_seats, "empty seats today.")


# more variables and playing with output
myName = "Emily"
myAge = 15
myHeight = 65 # inches
myEyes = "brown"
myHair = "yes, more"

print("Lets talk about %s." % myName)
print("She's %d inches tall." % myHeight)
print("she's got %s eyes and %s hair." % (myEyes, myHair))
print("if i add %d and %d, i get %d." % (myAge, myHeight, myAge+myHeight))

# playing with the output on my own

theName = "dog"
theAge = 13
theHeight = 12 # inches
theEyes = "brown"
theHair = "yes, some"

print("Lets talk about %s." % theName)
print("He's %d inches tall." % theHeight)
print("he's got %s eyes and %s hair." % (theEyes, theHair))
print("if i add %d and %d, i get %d." % (theAge, theHeight, theAge+theHeight))

