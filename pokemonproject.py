person = input ("Enter your name: ")

print(person,'Welcome to Pokemon World! When you catch one pokemon successfully, you will earn 5 credits. In room one, you can catch grass pokemons. when you had earned 20 credits in room one then you can go to room two and catch fire pokemons. Again, when you had earned 30 points in room two, then you can go to room three and catch all types of pokemons! Enjoy!' )

print("welcome to room 1! You can catch grass pokemon now!")

Bulbasaur = input("Do you wan to catch Bulbasaur?")

if Bulbasaur == "yes":
    print("********* waiting for the result**********")
    print("Congratulations! Bulbasuar is in your bag!")
    print("You recieve 5 credits!")
else:
    print("Ok Bulbasaur escapes...")
    
Tangela = input("Do you want to catch Tangela?")

if Tangela == "yes":
    print("********* waiting for the result**********")
    print("Congratulations! Tangela is in your bag!")
    print("You recieve 5 credits!")
    if Bulbasaur == "yes":
         print("You have a total of 10 credits!")
else:
    print("Ok Tangela escapes.....")
