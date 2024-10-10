import matplotlib.pyplot as plt
from math import *
from decimal import Decimal, getcontext
import decimal
import sys
import mpmath

# Increase the maximum number of digits for int conversion
sys.set_int_max_str_digits(228505 + 1)  # +1 to ensure the given number is not too low

path='Calc-Start-Coordinate.txt'
# direction=Decimal(input("Direction: If traverse down, input 1, traverse up -1 :"))
# total_repetition=int(input("Total repetitions:"))
y=0
step=Decimal(750100./325)

decimal.getcontext().prec = 218510
mpmath.mp.dps = 220000


def calculate_large_power_digits(base, exponent):
     # Set precision high enough to handle the large number
    getcontext().prec = exponent

    # Calculate the large power
    result = Decimal(base) ** Decimal(exponent)

    return str(result)

def calculate_exponent(file_path):
    try:
        with open(file_path, 'r') as file:
            start_coordinate_str = file.read().strip()
        
        # print("start_coordinate_str", start_coordinate_str)
        # Increase the maximum number of digits for int conversion
        sys.set_int_max_str_digits(220000)  # ensure the given number is not too low
        
        # Input start coordinate
        start_coordinate = int(start_coordinate_str)
        
        # Covert start coordinate to a high-precision floating-point number
        start_coordinate = mpmath.mpf(start_coordinate)
        
        # Verify start coordinate
        if start_coordinate <= 0:
            raise ValueError("The number must be positive.")


        # print("start-coordinate-int", start_coordinate)
        # Calculate the exponent
        # exponent = log(start_coordinate, 2)
        exponent = mpmath.log(start_coordinate) / mpmath.log(2)

        # print("exponent", exponent)
        # with open("start-coordinate-calculation.txt", "w") as file:
        #     file.write(f"{exponent}")
        return exponent
    
    except FileNotFoundError:
        print(f"The file {file_path} does not exist.")
    except ValueError as ve:
        print(f"Value error: {ve}")
    except Exception as e:
        print(f"An error occurred: {e}")

def calculate_number_of_digits(exponent):
    # Calculate the number of digits
    # print("exponent", exponent)
    print("Calculating Start-Coordinate...")
    base = mpmath.mpf(2)

    result = mpmath.power(base, exponent)

    # Convert the result to an integer
    integer_result = int(result)
    # Convert the result to string and remove any scientific notation
    # result_str = mp.nstr(result, mp.dps, strip_zeros=False)
    # print(result_str)
    return integer_result

# Function to round an mpf number to a specific number of decimal places
def round_mpf(number, decimal_places):
    rounded_str = mpmath.nstr(number, decimal_places + 1)
    return mpmath.mpf(rounded_str)

def draw(end):

    with open(path, "w") as file:
        file.write(f"Start Coordinate From Terminate Coordinate: 2^{round_mpf(end, 10)}")
    digits = calculate_number_of_digits(end)
    with open("Calc-Start-Coordinate-By-Integer.txt", "w") as file:
        file.write(f"{digits}")

def cal(n,b,y):
    with open("Deviatioin.txt", "r") as file:
        deviation = file.read().strip()
    
    print("Calculating Start-Coordinate...")
    start_coordinate = calculate_exponent("Terminate-coordinate-integer.txt")
    if(start_coordinate): 
        print("Read Terminate-coordinate Success.")
    # start_coordinate = mpmath.mpf(start_coordinate_str)

    start_coordinate = start_coordinate + mpmath.mpf(deviation)
    # print("start-coordinate", start_coordinate)
    point=start_coordinate

    for _ in range(n):
        q=point+step
        next=point+b*step
        point=next 
        y=y+b*step
    return point

with open(path, "w") as file:
    file.write("")
# end = cal(total_repetition,direction,y)
# draw(end)
with open("terminate-coordinate.txt", "r") as file:
    terminate_coordinate = int(file.read().strip())
with open("pattern.json", "r") as file:
    result_binary = int(file.read().strip())
start_coordinate =  terminate_coordinate ^ result_binary

with open(path, "w") as file:
    file.write(f"{start_coordinate}")
# print("first point =>",f"2^{start_coordinate}")