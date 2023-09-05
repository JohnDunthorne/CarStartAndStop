command = ""
started = False
# while (command != "quit"): <<<this is derivative you can easily write | while True |
while True:
    # put .lower at the input and the string will always return a lowercase value
    # therefore no .lower() module is needed for this entry from here on.
    command = input("> ").lower()
    if command == "start":
        if started:
            print("The car is already started")
        else:
            started = True
            print("car has started")
    elif command == "stop":
        if not started:
            print("The car is already stopped")
        else:
            started = False
            print("Car has stopped")
    elif command == "help":
        # use triple quotes for multiline text
        print("""
type "start" to start the car
type "stop" to stop the car
type "quit" to finish playing
        """)
    elif command == "quit":
        quit_option = input("would you like to quite? Y or N: ").upper()
        if quit_option == "Y":
            break
        elif quit_option == "N":
            print("okay we wont quit :)")
        else:
            print("Invalid option, please pick Y or N: ")

        # break terminates a program

    else:
        print("Not a valid input")
