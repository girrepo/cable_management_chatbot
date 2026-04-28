while True:
    print("Wanna do cable management? [y/n]")
    cable_management = input().strip().lower()
    if cable_management == "y":
        print("Yay! Let's manage cables!")
        break
    elif cable_management == "n":
        while True:
            print("Wanna have some fun? [y/n]")
            fun = input().strip().lower()
            if fun == "y":
                print("Wise choice! Let's manage cables!")
                break
            elif fun == "n":
                print(":(")
                break
            else:
                print("invalid answer, type [y] or [n]")
        break
    else:
        print("invalid answer, type [y] or [n]")
print()
print()
print("The End!")
print("You can now close the window.")
input()