#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the solve function below.

def solve(s):
    words=s[:].split()
    for x in words:
        s = s.replace(x, x.capitalize())
    return s

if __name__ == '__main__':