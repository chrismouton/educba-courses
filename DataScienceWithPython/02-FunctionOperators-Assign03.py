# Assingment: Calculate the area of a regular polygon

import math

def main():
    number_of_sides = int(input("How many sides of the regular polygon: "))
    side_length = int(input("Waht is the length of a side of the regular polygon: "))


    area = (number_of_sides * side_length ** 2) * (0.25 * 1/math.tan(math.pi/number_of_sides))

    print(f"The area of the regular polygon is %0.3f" %area)

if __name__ == '__main__':
    main()
