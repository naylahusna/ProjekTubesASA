# Nama File : Algoritma.py
# Deskripsi : Implementasi algoritma UCS, GBFS, A*, Branch and Bound, dan Nearest Neighbor Heuristic
# Nama : Nayla Husna - 24060124140158
# Kelas : A

import copy
import copy
import heapq
from graph_init import adj_matrix, INF, get_heuristic

# fungsi untuk menentukan tetangga dari sebuah node
def get_neighbors(node):
    neighbors = []
    for j in range(len(adj_matrix[node])):
        if adj_matrix[node][j] != INF and adj_matrix[node][j] != 0:
            neighbors.append((j, adj_matrix[node][j]))
    return neighbors

# Algoritma Uniform Cost Search (UCS)
def ucs(start, goal):
    pq = [(0, start, [start])]
    visited = set()
    explored_order = []

    while pq:
        cost, node, path = heapq.heappop(pq)
        if node in visited: continue
        
        visited.add(node)
        explored_order.append(node)

        if node == goal:
            return path, cost, explored_order

        for neighbor, weight in get_neighbors(node):
            if neighbor not in visited:
                heapq.heappush(pq, (cost + weight, neighbor, path + [neighbor]))
    return None, INF, explored_order

# Algoritma Greedy Best-First Search (GBFS) 
def gbfs(start, goal):
    pq = [(get_heuristic(start, goal), start, 0, [start])]
    visited = set()
    explored_order = []

    while pq:
        h, node, cost, path = heapq.heappop(pq)
        if node in visited: continue
        
        visited.add(node)
        explored_order.append(node)

        if node == goal:
            return path, cost, explored_order

        for neighbor, weight in get_neighbors(node):
            if neighbor not in visited:
                heapq.heappush(pq, (get_heuristic(neighbor, goal), neighbor, cost + weight, path + [neighbor]))
    return None, INF, explored_order

# Algoritma A* Search
def astar(start, goal):
    pq = [(get_heuristic(start, goal), start, 0, [start])]
    visited = set()
    explored_order = []

    while pq:
        f, node, g, path = heapq.heappop(pq)
        if node in visited: continue
        
        visited.add(node)
        explored_order.append(node)

        if node == goal:
            return path, g, explored_order

        for neighbor, weight in get_neighbors(node):
            if neighbor not in visited:
                g_new = g + weight
                f_new = g_new + get_heuristic(neighbor, goal)
                heapq.heappush(pq, (f_new, neighbor, g_new, path + [neighbor]))
    return None, INF, explored_order

def reduce_matrix(matrix):
    mat = copy.deepcopy(matrix)
    n = len(mat)
    lb = 0
    # Baris
    for i in range(n):
        row = [mat[i][j] for j in range(n) if mat[i][j] != INF]
        if row:
            m = min(row)
            lb += m
            for j in range(n):
                if mat[i][j] != INF: mat[i][j] -= m
    # Kolom
    for j in range(n):
        col = [mat[i][j] for i in range(n) if mat[i][j] != INF]
        if col:
            m = min(col)
            lb += m
            for i in range(n):
                if mat[i][j] != INF: mat[i][j] -= m
    return mat, lb

# Algoritma Branch and Bound 
def branch_and_bound(matrix, start):
    n = len(matrix)
    initial_mat = copy.deepcopy(matrix)
    for i in range(n): initial_mat[i][i] = INF
    
    red_init, lb_init = reduce_matrix(initial_mat)
    pq = [(lb_init, 0, start, [start], red_init)]
    
    best_cost = INF
    best_route = None
    nodes_explored = 0

    while pq:
        lb, level, curr_node, path, curr_mat = heapq.heappop(pq)
        nodes_explored += 1
        
        if lb >= best_cost: continue

        if level == n - 1:
            return_cost = matrix[curr_node][start]
            if return_cost != INF:
                total = lb 
                if total < best_cost:
                    best_cost = total
                    best_route = path + [start]
            continue

        for next_node in range(n):
            if next_node not in path and curr_mat[curr_node][next_node] != INF:
                nm = copy.deepcopy(curr_mat)
                edge_cost = curr_mat[curr_node][next_node]
                
                for k in range(n):
                    nm[curr_node][k] = INF
                    nm[k][next_node] = INF
                nm[next_node][start] = INF
                
                nm_reduced, red_lb = reduce_matrix(nm)
                new_lb = lb + edge_cost + red_lb
                
                if new_lb < best_cost:
                    heapq.heappush(pq, (new_lb, level + 1, next_node, path + [next_node], nm_reduced))

    return best_route, best_cost, nodes_explored

# Algoritma Nearest Neighbor Heuristic (NNH)
def nearest_neighbor(start):
    n = len(adj_matrix)
    visited = [False] * n
    current = start
    visited[current] = True
    route = [current]
    total_cost = 0
    explored_nodes = [current] 

    for _ in range(n - 1):
        best_cost = INF
        best_next = -1
        
        for j in range(n):
            if not visited[j] and adj_matrix[current][j] != INF and adj_matrix[current][j] != 0:
                if adj_matrix[current][j] < best_cost:
                    best_cost = adj_matrix[current][j]
                    best_next = j
                    
        if best_next == -1:
            return None, INF, explored_nodes 
            
        total_cost += best_cost
        visited[best_next] = True
        route.append(best_next)
        explored_nodes.append(best_next)
        current = best_next

    return_cost = adj_matrix[current][start]
    if return_cost != INF:
        total_cost += return_cost
        route.append(start)
        explored_nodes.append(start)
    else:
        return None, INF, explored_nodes 

    return route, total_cost, explored_nodes