def create_adjacency_list():
    return {}

def add_edge_list(graph, u, v):
    if u not in graph:
        graph[u] = []
    if v not in graph:
        graph[v] = []
    graph[u].append(v)
    graph[v].append(u)

def remove_edge_list(graph, u, v):
    if u in graph:
        graph[u].remove(v)
    if v in graph:
        graph[v].remove(u)

def display_list(graph):
    for node, neighbors in graph.items():
        print(f"{node}: {neighbors}")
