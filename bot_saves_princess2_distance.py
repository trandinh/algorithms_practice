
move_steps = {'LEFT':(0, -1), 'RIGHT':(0, 1), 'UP':(-1, 0), 'DOWN':(1, 0)}
def get_neigbors(n, position):
    neighbors = []
    for key in move_steps:
        new_position = (position[0]+move_steps[key][0], position[1]+move_steps[key][1])
        if 0<= new_position[0]<n and 0<= new_position[1]<n:
            neighbors.append((key, new_position))
    return neighbors
    
def distance(p1, p2):
    return (abs(p1[0]-p2[0]) + abs(p1[1]-p2[1]))

def search_pricess(n, grid):
    for i in range(n):
        if 'p' in grid[i]:
            return (i, grid[i].index('p'))
        

def nextMove(n,r,c,grid):
    m_ps = (r, c)
    princess_ps = search_pricess(n, grid)
    #get neighbors of m 
    neighbors = get_neigbors(n, m_ps, )
    
    min_distance = float('inf')
    min_move = None 
    #calculate the distance from neigbor position to princess position
    for (key, n_position) in neighbors:
        d = distance(n_position, princess_ps)
        if d < min_distance:
            min_distance = d
            min_move = key
    
    return min_move
  
#output: Output only the next move you take to rescue the princess. Valid moves are LEFT, RIGHT, UP or DOWN
n = 3
grid = [['-', '-', '-'], ['-', 'm', '-'], ['p', '-', '-']]

print(nextMove(n, 2, 1, grid))

