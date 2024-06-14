# control structure directs the order of execution of the statements in a program
if country == "India":
    if state == "Kerala":
        print("India-Kerala")
else:
    print("India-Other")


# switch case statement
# A switch statement is a multiway branch statement that compares the value of a variable to the values specified in case statements.
# Python language doesn’t have a switch statement.
# Python uses dictionary mapping to implement Switch Case in Python
def switchExample(arg):
    switcher =  {
        0: "This is case zero",
        1: "This is case one",
        2: "This is case two"
    }
    return switcher.get(arg, "nothing")

if __name__ == "__main__":
    arg = 1
    print(switchExample(arg))


# match case statement
# structural pattern matching 
command = "Hello, world"
match command:
    case "Hello, world":
        print("Hello")
    case "Goodbye, world":
        print("Bye")
    case other:
        print("No match")
