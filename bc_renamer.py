import argparse
import os
import sys


# ################ #
# Argument Parsing #
# ################ #

parser = argparse.ArgumentParser()
parser.add_argument('path', help='Path to the directory containing the files or the file itself')
parser.add_argument('format', help='The Format to rename the file to')
arguments = parser.parse_args()
