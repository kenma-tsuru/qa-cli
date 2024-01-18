import json
import random
from string import ascii_uppercase
from colorama import just_fix_windows_console, Fore, Back

just_fix_windows_console()

with open("qa.json", "r") as file:
    qa = json.load(file)

random.shuffle(qa)

score = 0

for i,q in enumerate(qa):
    
    print(i+1, q["question"])
    random.shuffle(q["options"])
    solution = -1
    
    for j, c in enumerate(q["options"]):
        print("\t", ascii_uppercase[j], c)
        if c == q["answer"]:
            solution = ascii_uppercase[j]
    
    ans = input("enter choices: ")
    
    if ans.upper() == solution:
        print(Fore.GREEN+"correct!"+Fore.RESET)
        score += 1
    else:
        print(Fore.RED+"incorrect!"+Fore.RESET)
        
print(Back.YELLOW+f"You got {score}/{len(qa)}"+Back.RESET)