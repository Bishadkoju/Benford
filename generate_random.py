import csv
import random
import argparse
parser = argparse.ArgumentParser()
parser.add_argument("--count", help="Number of random integers to be generated", type=int)
parser.add_argument("--max", help="Maximum value of random number", type=int)
args = parser.parse_args()
count = 10000
max = 999999
if(args.count):
    count = args.count
if(args.max):
    max = args.max
with open('random_numbers.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    for i in range(count):
        writer.writerow([random.randint(1, max)])