#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    N = int(input())
    if(N%2==0):
        if(N<=20 and N>=6):
            print('Weird')
        else:
            print('Not Weird')
    else:
        print('Weird')
Python If-Else
