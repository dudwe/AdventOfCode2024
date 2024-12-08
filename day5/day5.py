from collections import defaultdict

def read_file(file_name):
    """
    Read file in 2 chunks
    """
    page_ordering = []
    pages_to_produce = []
    with open(file_name, "r") as f:
        for x in f:
            if "|" in x:
                vals = x.split("|")
                rule = (int(vals[0]), int(vals[1]))
                page_ordering.append(rule)
            elif "," in x:
                vals = [int(v) for v in x.split(",")]
                pages_to_produce.append(vals)
        return page_ordering, pages_to_produce


def part_1():
    page_ordering, pages_to_produce = read_file("input.txt")
    #print(page_ordering)
    #print(pages_to_produce)

    '''
    Build a adjacency list
    '''
    adjList = defaultdict(list)
    for page in page_ordering:
        adjList[page[0]].append(page[1])
    #print(adjList)
    valid_updates = []
    for update in pages_to_produce:
        valid = True
        for ptr in range(len(update)-2,-1,-1):
            nxt = update[ptr+1]
            cur = update[ptr]
            if adjList[nxt] == []:
                #leaf is valid
                continue
            elif nxt not in adjList[cur]:
                valid = False
                break
        if valid:
            valid_updates.append(update)
    #print(valid_update)
    print(sum([update[int(len(update)/2)] for update in valid_updates ]))


def fix_update(update, adjList):
    #Get the number of children in path for each number. Use that to find the correct ordering
    valid_children = defaultdict(int)
    path_set = set(update)
    for elem in update:
        valid_children[elem] = len(list(filter(lambda x: x in path_set, adjList[elem])))
    sort_orders = sorted(valid_children.items(), key=lambda x: x[1], reverse=True)
    return ([x[0] for x in sort_orders])


def part_2():
    page_ordering, pages_to_produce = read_file("input.txt")


    '''
    Build a adjacency list
    '''
    adjList = defaultdict(list)
    for page in page_ordering:
        adjList[page[0]].append(page[1])
    print(adjList)
    invalid_updates = []
    for update in pages_to_produce:
        valid = True
        for ptr in range(len(update)-2,-1,-1):
            nxt = update[ptr+1]
            cur = update[ptr]
            if adjList[nxt] == []:
                #leaf is valid
                continue
            elif nxt not in adjList[cur]:
                valid = False
                break
        if not valid:
            invalid_updates.append(update)
    #To fix each invalid update
    mid_total = 0
    for update in invalid_updates:
        fixed_update = fix_update(update, adjList)
        print(update, "->", fixed_update)
        mid_total += fixed_update[int(len(fixed_update)/2)]
    print(mid_total)

part_1()
part_2()
