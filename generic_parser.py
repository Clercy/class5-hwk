#!/usr/bin/env python

# 1. load a dataset from a file
# 2. "organize" that file, so that we can access columns *or* rows of it easily
# 3. compute some "summary statistics" about dataset
# 4. print those summary statistics


# 1. load a dataset
# 1a. accept arbitrary filename as arhument
# 1b. load the file

from argparse import ArgumentParser

parser = ArgumentParser(description='A CSV reader +  stats maker')
#parser.add_argument('csvfile', help='Path to the input csv file.')

parser.add_argument('csvfile', help='Path to the input csv file.')
parsed_args = parser.parse_args()
print(parsed_args)
print(parsed_args.csvfile)

my_csv_file = parsed_args.csvfile

# Check if file exists

import os
import os.path as op

#if os.path.isfile(my_csv_file):
#	print("yay, it's real!")
#else:
#	print('oops, plz give rl files')


#Validate if file is tere or else abort here
assert op.isfile(my_csv_file), "Please give a real file,k thx"
print('Woot the file exists')



# 1b. load the file
import pandas as pd

data = pd.read_csv(my_csv_file, sep='\s+|,', header=None)
print(data.head())

#for item in dir(data):
#	print(item)

print(data.shape)

#  "organize" that file, so we can access columns *or* rows of it easily
# 2a. access any row
# 2b. access any column
# 2c. access any value

#all columns with specified rows
print(data.iloc[3:5,:])


print(data.iloc[:3,-3:])


print(data.iloc[3,4])


import numpy as np

print(np.mean(data))
print(np.std(data))
