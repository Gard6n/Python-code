#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input("Num ").strip())
    
if n%2 != 0:
    print('Weird')
    
if n%2 == 0 and n in range(2,5):
    print('Not Weird')
    
if n%2 == 0 and n in range(6,20):
    print('Weird')

if n%2 == 0 and n > 120:
    print('Not Weird')