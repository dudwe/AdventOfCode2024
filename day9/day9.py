
def read_file(file_name):
    """
    Read file as a 2d array
    """
    with open(file_name, "r") as f:
        for line in f:
            return [int(x) for x in line.strip()]


def part_1(input):
    '''
    We need to firstly read the input and alternate
    data_stack = []
    free_space_stack = []
    We fill the data_stack and free_space stack with our inital scan
    2333133121414131402
    On the stack we store: (block_value, starting_index, spaces_free)
    '''
    blocks = read_file(input)
    print(blocks)
    udata = []
    data = True
    data_value = 0
    for v in blocks:
        if data:
            udata += [data_value] * v
            data_value += 1
        else:
            udata += [-1] * v
        data = not data
    print(udata)

    free_ptr = 0
    data_ptr = len(udata) -1

    while free_ptr < data_ptr:
        while free_ptr < len(udata) and udata[free_ptr] != -1:
            free_ptr+=1
        while data_ptr > 0 and udata[data_ptr] == -1:
            data_ptr-=1            
        udata[free_ptr], udata[data_ptr] = udata[data_ptr], udata[free_ptr]
        data_ptr-=1
        free_ptr+=1
    print(udata)
    total = 0
    for idx, val in enumerate(udata):
        if val != -1:
            total += idx * val

    print(total)


class part_2():

    def __init__(self):
        self.udata = []
        self.cdata = []

    def compress(self, l, r, val):
        """
        Find a free spot in cdata and move the block from (l, r).
        """
        data_length = r - l + 1  # File size
        start = 0
        while start < l:
            # Check if this span is free
            end = start
            if self.cdata[start] == -1:
                if all(self.cdata[i] == -1 for i in range(start, start + data_length)):
                    # Move the data to this span
                    for i in range(data_length):
                        self.cdata[start + i] = val
                    # Mark the original location as free
                    for i in range(l, r + 1):
                        self.cdata[i] = -1
                    return  # Exit after moving one file
                else:
                    while self.udata[end] < l and self.udata[end]  == -1:
                        end +=1
                    start = end
            else:
                start+=1

    def solve(self, input):
        blocks = read_file(input)
        #print(blocks)
        data = True
        data_value = 0
        for v in blocks:
            if data:
                self.udata += [data_value] * v
                data_value += 1
            else:
                self.udata += [-1] * v
            data = not data
        #print(self.udata)
        self.cdata = self.udata[:]
        
        r = len(self.udata) -1
        l =  len(self.udata) -1
        print(self.udata)
        while r >= 0:
            while self.udata[r] == -1 and r>=0:
                r-=1
            val = self.udata[r]
            l = r -1 
            while self.udata[l] == self.udata[r] and l >= 0:
                l -=1
            l+=1
            print("Try to move",l,r, val)
            self.compress(l,r,val)
            r = l -1
            #print(self.cdata)

        total = 0
        for idx, val in enumerate(self.cdata):
            if val != -1:
                total += idx * val
        print(total)

input = "input.txt"
#part_1(input)
solver = part_2()
solver.solve(input)
#5989780676146 is too low....
#6351878974088 too high
#6351801932670
#6351801932670