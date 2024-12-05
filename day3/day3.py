import csv
import csv


def read_file(file_name):
    with open(file_name, "r") as f:
        data = [x for x in f]
        return data

def part_1():
    data = read_file("input.txt")
    ptr = 0
    total = 0
    for line in data:
        ptr = 0

        while ptr < len(line):
            prefix = line[ptr:ptr+4]
            if prefix == "mul(":
                #Test if we have NNN,NNN) patter
                stack = [""]
                valid_mul = True
                ptr+=4
                while ptr < len(line):
                    if line[ptr].isnumeric():
                        #Read the next 3 chars..
                        if stack[-1] == "":
                            if line[ptr] == "0":
                                valid_mul = False
                                break
                        if len(stack[-1]) == 3:
                            valid_mul = False
                            break
                        else:
                            num = stack.pop()
                            num += line[ptr]
                            stack.append(num)

                    elif line[ptr] == ',':
                        if len(stack) != 1:
                            valid_mul = False
                            break
                        stack.append("")
                    elif line[ptr] == ")" :
                        if len(stack) == 2:
                            
                            break
                        else:
                            valid_mul = False
                            break
                        
                    else:
                        valid_mul = False
                        break
                    ptr+=1
                if valid_mul:
                    total += int(stack[0])  * int(stack[1])
            ptr+=1
    print(total)
            


def part_2():
    '''
    Same as before but we need to handle:
        do() enable future mul
        don't() ignore future mul
        lets assume the do/dont is global and carries accross lines 
    '''
    data = read_file("input.txt")
    ptr = 0
    total = 0
    enable = True
    for line in data:
        ptr = 0
        while ptr < len(line):
            if line[ptr:ptr+4] == "mul(" and enable: 
                print("Test to see if valid pair")
                stack = [""]
                valid_mul = True
                ptr+=4
                while ptr < len(line):
                    if line[ptr].isnumeric():
                        #Read the next 3 chars..
                        if stack[-1] == "":
                            if line[ptr] == "0":
                                valid_mul = False
                                break
                        if len(stack[-1]) == 3:
                            valid_mul = False
                            break
                        else:
                            num = stack.pop()
                            num += line[ptr]
                            stack.append(num)
                    elif line[ptr] == ',':
                        if len(stack) != 1:
                            valid_mul = False
                            break
                        stack.append("")
                    elif line[ptr] == ")" :
                        if len(stack) == 2:
                            break
                        else:
                            valid_mul = False
                            break
                    else:
                        valid_mul = False
                        break
                    ptr+=1
                if valid_mul:
                    print("VALID MUL", stack)
                    total += int(stack[0])  * int(stack[1])
            elif line[ptr:ptr+4] == "do()":
                print("Enable")
                enable = True
            elif line[ptr:ptr+7] == "don't()":
                print("Disable")
                enable = False
            
            ptr+=1
    print(total)

part_1()
part_2()
