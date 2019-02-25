#!/usr/bin/env python

# 1. load a dataset from a file
# 2. "organize" that file, so that we can access columns *or* rows of it easily
# 3. compute some "summary statistics" about dataset
# 4. print those summary statistics


# 1. load a dataset
# 1a. accept arbitrary filename as arhument
# 1b. load the file

def thetimestamp ():

    now = datetime.datetime.now()
    thetimestamp = str(now.year) + str(now.month) + str(now.day) + str(now.hour) + str(now.minute) + str(now.second)
    return thetimestamp





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

#Validate if file is tere or else abort here
assert op.isfile(my_csv_file), "Please give a real file,k thx"
print('Woot the file exists')


# 1b. load the file
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import datetime

data = pd.read_csv(my_csv_file, sep='\s+|,', header=None)
data.columns = ["CRIM", "ZN", "INDUS", "CHAS", "NOX", "RM", "AGE", "DIS", "RAD", "TAX", "PTRATIO", "B1000", "LSTAT", "MEDV"]

#print(data.head())
#print(data.tail())
print(data)

#trying for sum
#data.loc[len(data)] = [data[col].sum() for col in data.columns]

#columns = list(data)
#for column in columns:
#    print (data[column])

#######to iterate over all columns but the first one
##for column in data.columns[1:]:
for column in data.columns:

    plt.plot(data[column])
    #print(data[column])# This is the column data to see
    plt.ylabel(column)
    #plt.show()
    #mp.savefig('foo.png')
    plt.savefig(column + '_'+ thetimestamp() + '.png')
    plt.close() # by using this I clear the plot cache or else it adds incrementally
#now = datetime.datetime.now()
#mytimestamp = str(now.year) + str(now.month) + str(now.day) + str(now.hour) + str(now.minute) + str(now.second)

#mytimestamp = thetimestamp()
#print(thetimestamp())
#print (mytimestamp)

print('Number of columns: ' + str(len(data.columns)))
print('Number of columns: ' + str(len(data.columns)))
print('Number of rows: ' + str(len(data.index)))



#print(data["CRIM"].mean())
#print(data.shape)
print(np.mean(data))
print(np.std(data))
