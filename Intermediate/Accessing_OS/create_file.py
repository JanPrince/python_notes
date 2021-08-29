"""
Exit Status / Return Code

    This script receives a file name as a command line argument. It first checks whether the file name exist or not,
    then creates the file if it doesn't exist.
"""

import os
import sys

filename = sys.argv[1]

if not os.path.exists(filename):
    with open(filename, 'w') as f:
        f.write("New file created\n")

else:
    print("Error, the file {} already exists!".format(filename))

# run this program from the terminal