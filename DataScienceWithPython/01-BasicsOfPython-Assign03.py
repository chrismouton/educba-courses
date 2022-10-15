# Assignment: Take the three sides as input from user; 
# Calculate the area using Heron's formula:
# sp=(s1+s2+s3)/2; 
# area = (sp*(sp-s1)*(sp-s2)*(sp-s3))**0.5

import math

def main():
    side1 = float(input("What is the length of the first side of the triangle: "))
    side2 = float(input("What is the length of the second side of the triangle: "))
    side3 = float(input("What is the length of the third side of the triangle: "))

    semi_perimeter = (side1 + side2 + side3)/2

    area = math.sqrt(semi_perimeter * (semi_perimeter - side1) * (semi_perimeter - side2) * (semi_perimeter - side3))

    print("The area of the triangle is %0.3f" %area)

if __name__ == '__main__':
    main()