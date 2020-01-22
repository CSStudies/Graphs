# Write a function that takes a 2D binary array and returns the number of 1 islands. 
# An island consists of 1s that are connected to the north, south, east or west. 
# For example:
# islands = [[0, 1, 0, 1, 0],
#            [1, 1, 0, 1, 1],
#            [0, 0, 1, 0, 0],
#            [1, 0, 1, 0, 0],
#            [1, 1, 0, 0, 0]]
# island_counter(islands) # returns 4

import util 

islands = [[0, 1, 0, 1, 0],
           [1, 1, 0, 1, 1],
           [0, 0, 1, 0, 0],
           [1, 0, 1, 0, 0],
           [1, 1, 0, 0, 0]]

let arry = []
for i in islands: 
    for j in islands[i]:
        if j = 1:
            new_tup = (i, j)
            arry.push(new_tup)

