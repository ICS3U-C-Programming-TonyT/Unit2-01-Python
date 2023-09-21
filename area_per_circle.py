#!/usr/bin/env python3

# Created by: Tony Tran
# Created on: September. 21, 2023
# This program does Area and Circumference.

import math

radius = 75
pi = math.pi
area = round(pi * (radius**2), 2)
circumference = round(2 * math.pi * radius, 2)
print(f"Area [π{radius}**2 = {area}]")
print(f"Circumference [2π{radius} = {circumference}]")
