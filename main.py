import numpy as np
import json
import matplotlib.pyplot as plt
import decimal
from decimal import Decimal, getcontext
from math import *
import sys
import mpmath
from mpmath import mp, log

path = []
polygons = []

# Set the precision (number of decimal places)
mp.dps = 250000
# Increase the maximum number of digits for int conversion
sys.set_int_max_str_digits(250000)  # ensure the given number is not too low

def decimal_to_binary(n):
    return bin(n).replace("0b", "")

def generate_powers_of_two(max_digits):
    powers_of_two = set()
    num = 1
    while len(str(num)) <= max_digits:
        powers_of_two.add(num)
        num <<= 1  # Efficient multiplication by 2 using bit shift
    return powers_of_two

def bitwise(int1, int2):
    return int1 ^ int2
# Function for reading start-coordinate.txt
def calculate_exponent(integer):
 
    try:
        # Covert start coordinate to a high-precision floating-point number
        value_mpf = mp.mpf(integer)

        # Calculate the exponent
        exponent = mpmath.log(value_mpf, b=2)

        return exponent
    
    except ValueError as ve:
        print(f"Value error: {ve}")
    except Exception as e:
        print(f"An error occurred: {e}")

def calculate_number_of_digits(exponent):
    # Calculate the number of digits
    # print("exponent", exponent)
    print("Calculating integer coordinate...")
    base = mp.mpf(2)

    result = mp.power(base, exponent)

    # Convert the result to an integer
    integer_result = int(result)
    # Convert the result to string and remove any scientific notation
    # result_str = mp.nstr(result, mp.dps, strip_zeros=False)
    # print(result_str)
    return integer_result

def write_json(path):
    json_data = json.dumps(path, indent=4, default=str)
    with open('pattern.json', 'w') as json_file:
        json_file.write(json_data)


def main():

    with open('pattern.json', "w") as file:
        file.write("")

    terminate_coordinate_exponent = input("Enter the exponents of the x-coordinate of the green line (e.g., for 2^400000 enter 400000): ")

    print("Reading start coordinate from start-coordinate.txt...")
    file_path = 'start-coordinate.txt'

    with open(file_path, 'r') as file:
        start_coordinate_str = file.read().strip()
        
    # Input start coordinate
    start_coordinate = int(start_coordinate_str)

    term_coor_int = calculate_number_of_digits(terminate_coordinate_exponent)
    # print("term_coor_int", term_coor_int)
    # Verify start coordinate
    term_coor_exp = int(terminate_coordinate_exponent) + 1

    print("term_coor_exp",term_coor_exp)


    result_binary = start_coordinate ^ term_coor_int

    write_json(result_binary)

    with open("terminate-coordinate.txt", "w") as file:
        file.write(f"{term_coor_int}")
    # if 2 ** start_exponent != start_coordinate:
    #     print("The x-coordinate of start point is not an exact power of 2. So an accuracy may be a little down.")
    # else:
    #     print("The x-coordinate of start point is an exact power of 2.")

    


if __name__ == "__main__":
    main()
