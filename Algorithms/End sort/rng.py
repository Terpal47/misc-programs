# Generates a .txt files containing random values seperated by commas.
# A generic program used to output random numbers to test sorting algorithms with.

from random import randint
import sys

NUM_NUMS = 23 # Number of values to generate
MAX_NUM = NUM_NUMS * 3 # Set upper limit
MIN_NUM = NUM_NUMS * -3 # Set lower limit
FILE_NAME = "rand_nums.txt"

file = open(FILE_NAME, 'w')

for i in range(NUM_NUMS):
    random_number = randint(MIN_NUM, MAX_NUM)
    file.write("{} ".format(random_number))
    #sys.stdout.write("{} ".format(random_number))

file.close()