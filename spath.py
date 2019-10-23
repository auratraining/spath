import json

def get_route_map(fname):
    rfd=open(fname,'r')
    ldata = []
    while(1):
        data = rfd.readline()
        #print (data)
        if (len(data) <= 0):
            break
        x = data.strip().split("\t")
        ldata.append(x)

    return ldata

def populate_entrance(rmap, map_table):
    count = 1
    for r, line in enumerate(rmap):
        for c, cell in enumerate(line):
            if (rmap[r][c] == 'E'):
                #print (r, c, rmap[r][c])
                map_table['Entrance'].append({f"T"+str(count):(r,c)}) 
                count = count + 1

def is_edge(rmap, r, c):
    if (rmap[r][c] == 'R'):
        if( (rmap[r-1][c]=='R' and rmap[r][c+1]=='R') or
            (rmap[r][c+1]=='R' and rmap[r+1][c]=='R') or
            (rmap[r][c-1]=='R' and rmap[r+1][c]=='R') or
            (rmap[r-1][c]=='R' and rmap[r][c-1]=='R')):
            #print (r, c, rmap[r][c])
            return True
    return False


def populate_edges(rmap, map_table):
    count = 1
    for r, line in enumerate(rmap):
        for c, cell in enumerate(line):
            if (is_edge(rmap, r, c)):
                map_table['Edges'].append({f"E"+str(count):(r,c)}) 
                count = count + 1

def is_in_edge_list(route_map, map_table, r, c):
    for entry in map_table["Edges"]:
        key, index = list(entry.items())[0]
        if (index == (r,c)):
            return True
    return False

def is_valid_cell(route_map, map_table, r, c):
    if (route_map[r][c] == 'w' or route_map[r][c] == 'E') :
        return False

    if (is_in_edge_list(route_map, map_table, r, c)):
        return False
    
    return True

def top_adjecent_nodes(route_map, map_table, r, c):
    i = r - 1
    j = c
    while(is_valid_cell(route_map, map_table, i, j)):
        #print (route_map[i][c], i, j)
        yield (i, j)
        i = i - 1

def right_adjecent_nodes(route_map, map_table, r, c):
    i = r
    j = c + 1

    while(is_valid_cell(route_map, map_table, i, j)):
        #print (route_map[r][j], i, j)


        yield (i, j)
        j = j + 1

def bottom_adjecent_nodes(route_map, map_table, r, c):
    i = r + 1
    j = c
    while(is_valid_cell(route_map, map_table, i, j)):
        #print (route_map[i][c], i, j)
        yield (i, j)
        i = i + 1

def left_adjecent_nodes(route_map, map_table, r, c):
    i = r
    j = c - 1
    while(is_valid_cell(route_map, map_table, i, j)):
        #print (route_map[r][j], i, j)
        yield (i, j)
        j = j - 1

def get_adjecent_nodes(route_map, map_table, r, c):
    adj_nodes = list(top_adjecent_nodes(route_map, map_table, r, c))
    print (f"top :{adj_nodes}", end=" ")

    adj_nodes = list(right_adjecent_nodes(route_map, map_table, r, c))
    print (f"right :{adj_nodes}", end=" ")

    adj_nodes = list(bottom_adjecent_nodes(route_map, map_table, r, c))
    print (f"bottom :{adj_nodes}", end=" ")

    adj_nodes = list(left_adjecent_nodes(route_map, map_table, r, c))
    print (f"left :{adj_nodes}", end="\n")

def populate_adjecencts(route_map, map_table):
    for entry in map_table["Edges"]:
        key, index = list(entry.items())[0]
        r, c = index
        print (key, r, c, end=":")
        get_adjecent_nodes(route_map, map_table, r, c)

def dump_data(map_table):
    print (json.dumps(map_table))

def main():
    map_table = {
            "Entrance" : [],
            "Edges" : [],
            "AdjacenyTable":{}
            }
    filename = "data.txt"
    route_map = get_route_map(filename)
    print (route_map)

    populate_entrance(route_map, map_table)
    populate_edges(route_map, map_table)
    print (map_table)  
    populate_adjecencts(route_map, map_table)

if (__name__ == "__main__"):
    main()
