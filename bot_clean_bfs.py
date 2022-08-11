move_steps = {'LEFT':(0, -1), 'RIGHT':(0, 1), 'UP':(-1, 0), 'DOWN':(1, 0)}
def get_neigbors(n, position, visited):
    neighbors = []
    for key in move_steps:
        new_position = (position[0]+move_steps[key][0], position[1]+move_steps[key][1])
        
        if 0<= new_position[0]<n and 0<= new_position[1]<n:
            if visited[new_position[0]][new_position[1]]!=1:
                neighbors.append((key, new_position))
    return neighbors

def track_back(parent, position):
    (key,p) = parent[position]
    path = key
    while p in parent.keys():
        (key,p) = parent[p]
        path = key
    return path

def search_dust(n, m_ps, grid):

    queue = [m_ps]
    grid[m_ps[0]][m_ps[1]] = 1
    parent = {}
    while queue:
        position = queue.pop(0) 
        #check the moved path
        #found dust
        if grid[position[0]][position[1]] == 'd':
            path = track_back(parent, position)
            return path
        
        grid[position[0]][position[1]] = 1
        neighbors = get_neigbors(n, position, grid)

        
        for (key, n_position) in neighbors:
            queue.append(n_position)
            parent[n_position] = (key, position)

def next_move(posr, posc, board):
    if board[posr][posc] == 'd':
        print('CLEAN')
    n = len(board)
    m_ps = (posr, posc)
    print(search_dust(n, m_ps, board))

posr = 0
posc = 0
board = [list("b---d"),
        list("-d--d"),
        list("--dd-"),
        list("--d--"),
        list("----d")]
print(board)

next_move(posr, posc, board)
