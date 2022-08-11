

move_steps = {'LEFT':(0, -1), 'RIGHT':(0, 1), 'UP':(-1, 0), 'DOWN':(1, 0)}
def get_neigbors(n, position, visited):
    neighbors = []
    for key in move_steps:
        new_position = (position[0]+move_steps[key][0], position[1]+move_steps[key][1])
        if 0<= new_position[0]<n and 0<= new_position[1]<n:
            if not visited[new_position[0]][new_position[1]]:
                neighbors.append((key, new_position))
    return neighbors
    
def track_back(parent, position, n):
    start = (int(n/2), int(n/2))
    (key,p) = parent[position]
    path = key
    while p in parent.keys():
        (key,p) = parent[p]
        path = key +'\n'+ path
    return path

def search(n, grid, m_ps, visited, queue):
    
    visited[m_ps[0]][m_ps[1]] = 1
    parent = {}
    while queue:
        # (key,position) = queue.pop(0) 
        position = queue.pop(0) 
        # print(parent)

        visited[position[0]][position[1]] = 1

        if grid[position[0]][position[1]] == 'p':
            return track_back(parent, position, n)
            # return

        neighbors = get_neigbors(n, position, visited)
        
        for (key, n_position) in neighbors:
            queue.append(n_position)
            parent[n_position] = (key, position)


def displayPathtoPrincess(n, grid):
    m_ps = (int(n/2), int(n/2))

    visited = [[0]*n for i in range(n)]
    visited[m_ps[0]][m_ps[1]] = 1
    queue = []
    queue.append(m_ps)
    print(search(n, grid, m_ps, visited, queue))
    
#output: Print out the moves you will take to rescue the princess in one go. 
#The moves must be separated by '\n', a newline. The valid moves are LEFT or RIGHT or UP or DOWN.
n = 3
grid = [['-', '-', '-'], ['-', 'm', '-'], ['p', '-', '-']]
displayPathtoPrincess(n, grid)
