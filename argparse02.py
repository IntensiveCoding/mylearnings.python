import argparse

parser = argparse.ArgumentParser()
parser.add_argument('throw', choices=['rock', 'paper', 'scissors'])
args = parser.parse_args()

# How to call
# python argparse02.py rock
# python argparse02.py scissors

print("~ Throw: {}".format(args.throw))
