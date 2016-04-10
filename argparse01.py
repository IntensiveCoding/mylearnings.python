import argparse

parser = argparse.ArgumentParser(description='Parsing arguments')

# Optional arguments with short and long flags
parser.add_argument('-s', '--sum', action='store_true', help='Sum the list of numbers')

# Optional arguments with required flag
parser.add_argument('-v', '--verbose', required=True, help='Verbose list')

# Positional arguments just specified without --
# Positional arguments are required arguments)
# nargs='*' - Return all parameters if present, or empty list if none
# nargs='+' - 1 or more parameters
# nargs='?' - Make a positional argument optional
parser.add_argument('add', type=int, nargs='+', default=20, help='Add numbers')

args = parser.parse_args()

if args.sum:
    print ('--sum found')
else:
    print ('--sum not found')

print ('args.sum: ', args.sum)
print ('args.add: ', args.add)
