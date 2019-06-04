import argparse

# parser = argparse.ArgumentParser()
# The default ACTION is to store the variable!
# parser.add_argument("echo", help="echo the string you use here")
# This pulls out every argument you feed it!
# args = parser.parse_args()
# This prints the string you chose to store by utilizing the argument added above!
# print(args.echo)

parser = argparse.ArgumentParser()
parser.add_argument("--verbosity", help="increase output verbosity")
args = parser.parse_args()
if args.verbosity:
    print("verbosity turned on")