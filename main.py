#!/usr/bin/env python3
import sys
import os
import json

debug = True;

with open("Dictonary.json", "r", encoding="utf-8") as file:
    Dictonary = json.load(file)
if debug:
    print(f"Pure Zeilen:{Dictonary}")
    
Request = input("English word (w. correct grammer!!): ")
if Dictonary.get(Request, None) == None:
    print("idk")
else:
    print(f"It means {Dictonary.get(Request)} in german")

with open("Dictonary.json", "w", encoding="utf-8") as file:
    json.dump(Dictonary, file, ensure_ascii=False, indent=4)