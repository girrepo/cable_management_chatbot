while True:
    
# prompting the user to decide if they want to do cable management
    print("Wanna do cable management? [y/n]")
    cable_management = input().strip().lower()

# validating the user's input and responding accordingly
    if cable_management == "y":
        print("Yay! Let's manage cables!")
        break
    elif cable_management == "n":
        while True:

# prompting the user to decide if they want to have fun
            print("Wanna have some fun? [y/n]")
            fun = input().strip().lower()

# validating the user's input and responding accordingly
            if fun == "y":
                print("Managing cables IS fun, dummy! Let's do it!")
                break
            elif fun == "n":
                print(":(")
                break

# handling invalid input for the fun question
            else:
                print("invalid answer, type [y] or [n]")
        break

# handling invalid input for the cable management question
    else:
        print("invalid answer, type [y] or [n]")

# concluding the conversation with a message
print()
print()
print("The End!")
print("You can now close the window.")
input()