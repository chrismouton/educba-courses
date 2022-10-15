# Assignment: Take the radious as input from the user
# and calculate the area using 3.14 as Pi

def main():
    radius = float(input("What is the radius of the circle you want me to calculate: "))

    area = 3.14 * radius ** 2

    print("The area of the circle is %0.2f" %area)

if __name__ == '__main__':
    main()