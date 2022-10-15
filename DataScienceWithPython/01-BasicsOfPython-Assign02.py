# Assignment: Take 2 numbers input from a user. 
# Print them before and after swapping.

def main():
    num1 = int(input("Please enter the first number: "))
    num2 = int(input("Please enter the second number: "))

    print("Before swapping:")
    print(f"num1 := {num1}")
    print(f"num2 := {num2}")
    print()

    temp = num1
    num1 = num2
    num2 = temp

    print("After swapping:")
    print(f"num1 := {num1}")
    print(f"num2 := {num2}")


if __name__ == '__main__':
    main()