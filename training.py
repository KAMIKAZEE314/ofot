#!/usr/bin/env python3
import os
import json
from random import randint

debug = False

while True:
    with open("Unsure.json", "r", encoding="utf-8") as file:
        unsure = json.load(file)
        unsure_list = list(unsure.keys())
    if debug:
        print(f"Pure Zeilen:{unsure}")
        
    if len(unsure) != 0:
        rand_index = randint(0, len(unsure_list) - 1)
        data = input(f"What's {unsure_list[rand_index]} in german: ")
        unsure[unsure_list[rand_index]].append(data)
        if len(unsure[unsure_list[rand_index]]) >= 13:
            data = unsure[unsure_list[rand_index]]
            same_copies = {}
            for data_piece in data:
                n_same_copies = -1 # -1 instead of 0 because counts itself as 1 same copy
                for data_piece_2 in data:
                    if data_piece == data_piece_2:
                        n_same_copies += 1
                same_copies[data_piece] = n_same_copies
            Dictionary[unsure_list[rand_index]] = max(same_copies, key=same_copies.get)
            del unsure[unsure_list[rand_index]]
                
    with open("Unsure.json", "w", encoding="utf-8") as file:
        json.dump(unsure, file, ensure_ascii=False, indent=4)