def create_adjacency_matrix(size):
    return [[0] * size for _ in range(size)]

def add_edge_matrix(matrix, u, v):
    matrix[u][v] = 1
    matrix[v][u] = 1  # For undirected graph

def remove_edge_matrix(matrix, u, v):
    matrix[u][v] = 0
    matrix[v][u] = 0

def display_matrix(matrix):
    for row in matrix:
        print(row)
