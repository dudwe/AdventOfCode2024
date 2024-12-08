from collections import defaultdict
import time
def read_file(file_name):
    """
    Read file as a 2d array
    """
    with open(file_name, "r") as f:
        data = [[char for char in x.strip()] for x in f]
        return data

directions = {"UP": (-1, 0), "DOWN": (1, 0), "LEFT": (0, -1), "RIGHT":  (0, 1)}
turn = {"UP": "RIGHT", "RIGHT": "DOWN", "DOWN": "LEFT", "LEFT": "UP"}

def part_1(input):
    '''
    We can use a path algo with counter
    We can do this iteratively rather than recursive
    We use a DFS with iterative stack 
        + Turn if facing wall
        + Stop if out of grid  
    '''

    grid = read_file(input)
    # Get starting location
    m , n = len(grid), len(grid[0])
    start_pos = (0, 0)
    for p in range(m):
        for q in range(n):
            if grid[p][q] == "^":
                start_pos = (p, q)

    #DFS to generat the walk

    guard = [start_pos[0], start_pos[1]]
    stack = [[guard, "UP"]]
    steps = 0
    visited_cells = set()
    while stack:
        guard_loc = stack.pop()
        #print(guard_loc, steps)
        guard_pos, guard_dir = guard_loc[0], guard_loc[1]
        visited_cells.add((guard_pos[0],guard_pos[1]))
        
        next_pos = guard_dir
        if grid[guard_pos[0]][guard_pos[1]] != "X":
            grid[guard_pos[0]][guard_pos[1]] = "X"
            steps+=1
        

        while True:
            next_step = [guard_pos[0] + directions[next_pos][0], guard_pos[1] + directions[next_pos][1]]
            if not(0 <= next_step[0] < m and 0 <= next_step[1] < n) :
                #for g in grid:
                #    print(''.join(g))
                return start_pos, steps, visited_cells
            if grid[next_step[0]][next_step[1]] != "#":
                break
            else:
                next_pos = turn[next_pos]
        stack.append([next_step, next_pos])
   

def dfs(grid, obstruction_cord, start_pos):
    stack = [[(start_pos[0], start_pos[1]), "UP"]]
    visited_cells = dict()
    m , n = len(grid), len(grid[0])
    while stack:
        guard_loc = stack.pop()
        guard_pos, guard_dir = guard_loc[0], guard_loc[1]
        next_pos = guard_dir
        if  (guard_pos) not in visited_cells:
            visited_cells[guard_pos] = {guard_dir}
        elif guard_dir in visited_cells[guard_pos]:
            return True
        else:
            visited_cells[guard_pos].add(guard_pos)

        while True:
            next_step = (guard_pos[0] + directions[next_pos][0], guard_pos[1] + directions[next_pos][1])
            if not(0 <= next_step[0] < m and 0 <= next_step[1] < n) :
                #for g in grid:
                #    print(''.join(g))
                return False
            if next_step == obstruction_cord or  grid[next_step[0]][next_step[1]] == "#":
                next_pos = turn[next_pos]
            else:
                break
                
        stack.append([next_step, next_pos])
    return True

def part_2(start_pos, input):
    '''
    Find the number of way we can obstruct the grid 
    Naive solution:
        For each VISITED cell we duplicate the grid and put a obstruction.
            Run the path_1 code, if we get stuck then obstruction works
            If we dont get stuck then we try another obstrucition 
        How do we know if we are stuck? 
            We visit the same cell with the same direction twice ! 
        
        Algo:
            Run part_1() code - get a list of all the visited nodes 
            for each visited coordinate:
                DFS(start_pos, new_obstruction)
                    in dfs we keep a 2d grid where each cell is ["X|.|#", ["UP", "DOWN",....]]


    '''
    grid = read_file(input)
    start_pos,_, visited_cells = part_1(input)
    valid_blocks = 0
    for visited_cell in visited_cells:
        #print("Place obstruction at ", visited_cell)
        if dfs(grid, visited_cell, start_pos):
            #print("VALID OBSTRUCTION:", visited_cell)
            valid_blocks+=1
    print(f"{valid_blocks=}")


input = "input.txt"
start_pos, steps, visited_cells = part_1(input)

print(f"{steps=}" )
part_2(start_pos, input)
