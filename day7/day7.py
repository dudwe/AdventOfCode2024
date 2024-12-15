
from collections import defaultdict
import time
def read_file(file_name):
    """
    Read file as a 2d array
    """
    with open(file_name, "r") as f:
        val_list = []
        targets = []
        for line in f:
            line = line.split(':')
            targets.append(int(line[0]))
            val_list.append([int(val) for val in line[1].split()])
        return targets, val_list

directions = {"UP": (-1, 0), "DOWN": (1, 0), "LEFT": (0, -1), "RIGHT":  (0, 1)}
turn = {"UP": "RIGHT", "RIGHT": "DOWN", "DOWN": "LEFT", "LEFT": "UP"}

def solve(target, val_list, current_val, ptr=0):

    if ptr == len(val_list) -1 :
        return current_val == target
    n = val_list[ptr+1]
    multi, adder = False, False
    if current_val * n <= target:
        multi = solve(target, val_list, current_val * n, ptr+1)
    if current_val + n <= target:
        adder = solve(target, val_list, current_val + n, ptr+1)
    return multi or adder
     

def part_1(input):
    target, vals = read_file(input)
    '''
    We can use a exhaustive search to see if we can compute the target:
        We can use recursion for this!

    '''
    total = 0
    for idx, val_list in enumerate(vals):
        if (solve(target[idx], val_list, val_list[0])):
            print("VALID COMBO!", target[idx])
            total += target[idx]
    print(f"{total=}")
        

def solve_2_wrapper(target, val_list):
    a = solve_2(target, val_list, val_list[0], 0)
    b = solve_2(target, val_list, int(str(val_list[0]) + str(val_list[1])), 1)
    return a or b

def solve_2(target, val_list, current_val, ptr=0):
    if ptr+1 == len(val_list) :
        return current_val == target
    
    n = val_list[ptr+1]
    multi, adder, comb = False, False, False

    comb_val = int(str(current_val) + str(n))
    if comb_val <= target:
        #print("TRY COMB:",target, val_list, comb_val, ptr+1)
        comb = solve_2(target, val_list, comb_val, ptr+1)

    if current_val * n <= target:
        multi = solve_2(target, val_list, current_val * n, ptr+1)
    if current_val + n <= target:
        adder = solve_2(target, val_list, current_val + n, ptr+1)
    #Try doing a comb operation


    return multi or adder or comb
     
def part_2(input):
    target, vals = read_file(input)
    total = 0
    for idx, val_list in enumerate(vals):

        if (solve_2_wrapper(target[idx], val_list)):
            print("VALID COMBO!", target[idx])
            total += target[idx]
    print(f"{total=}")

input = "input.txt"
part_2(input)
