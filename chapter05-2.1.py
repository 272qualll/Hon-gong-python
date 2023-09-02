#table-sharing arrangement
'''  before note taking
all_people = 12
counter = 0

def graph(node, before_edge_number):
    global counter
    if node == 0:
        counter += 1
    for i in range(max(2, before_edge_number), min(10, node) + 1):
        graph(node - i, i)
    
graph(all_people, 0)
print(counter)
'''

#after note taking
all_people = 6
memo = {}

def graph(node, before_edge_number):
    if (node, before_edge_number) in memo:
        return memo[(node, before_edge_number)]
        
    rtimes = 0
    if node == 0:
        rtimes += 1
    else:
        for i in range(max(2, before_edge_number), min(10, node) + 1):
            rtimes += graph(node - i, i)
    memo[(node, before_edge_number)] = rtimes
    return rtimes
    
print(graph(all_people, 0))
