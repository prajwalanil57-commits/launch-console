name = input("What's your name? ")
print("Welcome to " + name + "'s Launch Console!")

running = True
while running:
    print("1) About me")
    print("2) My goals")
    print("3) Fun fact")
    print("4) Exit")
    
    choice = input("Pick 1-4: ")
    
    if choice == "1":
        print("I'm a highschool student at Round Rock High, and enrolled in Elite 101 for CodetoCollege.")
    elif choice == "2":
        print("My goal: Is to learn more about coding and complete my first project this period.")
    elif choice == "3":
        print("Fun fact: I love coding interactive projects and I'm a black belt in karate")
    elif choice == "4":
        print("Goodbye!")
        running = False
    else:
        print("Please pick 1, 2, 3, or 4.")