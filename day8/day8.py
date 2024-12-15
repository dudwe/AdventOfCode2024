
from collections import defaultdict
import time
def read_file(file_name):
    """
    Read file as a 2d array
    """
    with open(file_name, "r") as f:
        antennas = defaultdict(list)
        M, N = 0,0
        for row, row_vals in enumerate(f):
            M = row
            for col, col_val in enumerate(row_vals.strip()):
                if col_val != '.':
                    antennas[col_val].append((row,col))
                N = col
        print(M,N,antennas)
        return M, N, antennas


def find_two_antinodes(coord_a, coord_b, M, N, antinodes):
    '''
    Gets list of anti nodes
    '''
    delta_x = coord_a[0] - coord_b[0]
    delta_y = coord_a[1] - coord_b[1]
    #print(f"Deltas {delta_x=} {delta_y=}")

    (ptr_x, ptr_y) = coord_a
    while(0<= ptr_x < M and 0 <=ptr_y < N):
        ptr_x , ptr_y = ptr_x + delta_x, ptr_y + delta_y
        if (ptr_x, ptr_y) not in [coord_a, coord_b] and 0<= ptr_x <= M and 0 <=ptr_y <= N:
            #print("PLOT",ptr_x, ptr_y)
            antinodes.add((ptr_x, ptr_y))
            break

    delta_x = -delta_x
    delta_y = -delta_y
    (ptr_x, ptr_y) = coord_a
    #print(f"Deltas {delta_x=} {delta_y=}")
    while(0<= ptr_x <= M and 0 <=ptr_y <= N):
        ptr_x , ptr_y = ptr_x + delta_x, ptr_y + delta_y
        if (ptr_x, ptr_y) not in [coord_a, coord_b] and 0<= ptr_x <= M and 0 <=ptr_y <= N:
            #print("PLOT",ptr_x, ptr_y)
            antinodes.add((ptr_x, ptr_y))
            break

def find_all_antinodes(coord_a, coord_b, M, N, antinodes):
    '''
    Gets list of anti nodes
    '''
    delta_x = coord_a[0] - coord_b[0]
    delta_y = coord_a[1] - coord_b[1]
    #print(f"Deltas {delta_x=} {delta_y=}")

    (ptr_x, ptr_y) = coord_a
    while(0<= ptr_x < M and 0 <=ptr_y < N):
        ptr_x , ptr_y = ptr_x + delta_x, ptr_y + delta_y
        if   0<= ptr_x <= M and 0 <=ptr_y <= N:
            #print("PLOT",ptr_x, ptr_y)
            antinodes.add((ptr_x, ptr_y))

    delta_x = -delta_x
    delta_y = -delta_y
    (ptr_x, ptr_y) = coord_a
    #print(f"Deltas {delta_x=} {delta_y=}")
    while(0<= ptr_x <= M and 0 <=ptr_y <= N):
        ptr_x , ptr_y = ptr_x + delta_x, ptr_y + delta_y
        if  0<= ptr_x <= M and 0 <=ptr_y <= N:
            #print("PLOT",ptr_x, ptr_y)
            antinodes.add((ptr_x, ptr_y))

     

def part_1(input):
    '''
    We need to build a list of antenna coordinates

    From there we need to compute the delta_x and delta_y
        We can then use this to find out how many antinodes we can plot
    '''

    M, N, antennas = read_file(input)
    antinodes= set()

    for antenna in antennas:
        print(f"Find antinodes for {antenna}")
        antenna_coords = antennas[antenna]
        #We need to now find all possible coordinates we can plot on the grid given 2 coords
        for idx, coord_a in enumerate(antenna_coords):
            for ptr in range(idx+1, len(antenna_coords)):
                coord_b = antenna_coords[ptr]
                #print("Resolve for", coord_a, coord_b)
                find_two_antinodes(coord_a, coord_b, M, N, antinodes)

    print(f" {len(antinodes)=} {antinodes=}")


     
def part_2(input):
    '''
    Same as part 1, we just remove the checks 
    '''
    M, N, antennas = read_file(input)
    antinodes= set()
    for antenna in antennas:
        print(f"Find antinodes for {antenna}")
        antenna_coords = antennas[antenna]
        #We need to now find all possible coordinates we can plot on the grid given 2 coords
        for idx, coord_a in enumerate(antenna_coords):
            antinodes.add(coord_a)
            for ptr in range(idx+1, len(antenna_coords)):
                coord_b = antenna_coords[ptr]
                #print("Resolve for", coord_a, coord_b)
                find_all_antinodes(coord_a, coord_b, M, N, antinodes)

    print(f" {len(antinodes)=} {antinodes=}")

input = "input.txt"
part_1(input)
part_2(input)