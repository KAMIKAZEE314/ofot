#!/usr/bin/env python3
import sys
import os

debug = True;

with open("Dictonary.txt", "r") as file:
    Content = file.readlines() 
if debug:
    print(f"Pure Zeilen:{Content}")