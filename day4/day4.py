def read_file(file_name):
    """
    Read file as a 2d array
    """
    with open(file_name, "r") as f:
        data = [[char for char in x.strip()] for x in f]
        return data


def part_1():
    data = read_file("input.txt")
    sols, row_matches, col_matches, diag_matches = 0, 0, 0, 0
    matches = [["X", "M", "A", "S"], ["S","A","M","X"]]
    # Search by row
    for row in data:
        for c in range(len(row)):
            if row[c : min(c+4, len(row))] in matches:                
                row_matches += 1
    print(data)    
    print(f"{row_matches=}")

    # Search by column
    for r in range(len(data[0])):
        for c in range(len(data)):
            col_string = [data[p][r] for p in range(c,min(c+4, len(data)))] 
            if col_string in matches:
               col_matches+=1
    print(f"{col_matches=}")

    # Search by diagonal l -> r 
    r = 0
    while r < len(data):
        c = 0
        while c < len(data[0]):
            word = []
            x, y = r, c
            while len(word) < 4 and x < len(data) and y < len(data[0]):
                word.append(data[x][y])
                x += 1
                y += 1
            if word in matches:
                diag_matches+=1
            c+=1
        r+=1
    print(f"{diag_matches=}")

    # Search by diagonal r -> l
    r = 0
    while r < len(data):
        c = len(data[0]) -1
        while c > 0:
            word = []
            x, y = r, c
            while len(word) < 4 and x < len(data) and y >= 0:
                word.append(data[x][y])
                x+=1
                y-=1
            if word in matches: 
                diag_matches+=1
            c-=1
        r+=1
            


    print(f"{diag_matches=}")
    sols = row_matches + col_matches + diag_matches
    print(f"{sols=}")




def part_2():
    """
    Do similar to before
        This time we scan for the letter "A"
        Then check to see if the two diagonals are valid 
        S       M
            A
        S       M

        M       M
            A
        S       S

        S       S
            A
        M       M

        M       S
            A
        M       S

    """
    data = read_file("input.txt")
    valid = [['S','A','M'], ['M','A','S']]
    count = 0
    for r in range(1,len(data)-1):
        for c in range(1, len(data[0])-1):
            if data[r][c] == "A":
                #Get l -> r diag
                lr_diag = [data[r-1][c-1], data[r][c], data[r+1][c+1]]
                #Get r -> l diag
                rl_diag = [data[r-1][c+1], data[r][c], data[r+1][c-1]]
                if lr_diag in valid and rl_diag in valid:
                    #print("FOUND VALID  XMAS :)")
                    count+=1
    print(count)


part_1()
part_2()
