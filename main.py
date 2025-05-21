#!/usr/bin/env python3
import sys
import os
import json

debug = True;

with open("Dictonary.json", "r", encoding="utf-8") as file:
    Dictonary = json.load(file)
if debug:
    print(f"Pure Zeilen:{Dictonary}")

with open("Unsure.json", "r", encoding="utf-8") as file:
    unsure = json.load(file)
    unsure_list = list(unsure.keys())
if debug:
    print(f"Pure Zeilen:{unsure}")

Request = input("English word (w. correct grammer!!): ")
if Dictonary.get(Request, None) == None:
    print("idk")
    if unsure.get(Request, None) == None:
        unsure[Request] = []
else:
    print(f"It means {Dictonary.get(Request)} in german")
    
data = input(f"What's {unsure_list[0]} in german: ")
unsure[unsure_list[0]].append(data)
if len(unsure[unsure_list[0]]) == 13:
    data = unsure[unsure_list[0]]
    lowercase_data = []
    for data_piece in data:
        lowercase_data.append(data_piece.lower())

with open("Dictonary.json", "w", encoding="utf-8") as file:
    json.dump(Dictonary, file, ensure_ascii=False, indent=4)
    
with open("Unsure.json", "w", encoding="utf-8") as file:
    json.dump(unsure, file, ensure_ascii=False, indent=4)