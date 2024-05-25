def are_nodes_adjacent(adj_matrix, node1, node2):
    """
    To Find:
    Determine if two nodes are adjacent in an undirected graph.
    
    Things To Remember:
        adj_matrix : The adjacency matrix representing the graph.
        node1 : The index of the first node.
        node2 : The index of the second node.
        
    Returns or Result:
        boolean: True if the nodes are adjacent, False otherwise.
    """
    # Check if the indices are valid
    num_nodes = len(adj_matrix)
    if node1 < 0 or node2 < 0 :
        raise ValueError("Invalid node indices")
    
    # Result
    return adj_matrix[node1][node2] == 1 or adj_matrix[node2][node1] == 1

# Example 1
adj_matrix = [
    [0, 1, 0, 0],
    [1, 0, 1, 1],
    [0, 1, 0, 1],
    [0, 1, 1, 0]
]
print('Node 0 and 1 Are Adjacent? ',are_nodes_adjacent(adj_matrix, 0, 1))  # True
print('Node 0 and 2 Are Adjacent? ',are_nodes_adjacent(adj_matrix, 0, 2))  # False

# Example 2
adj_matrix = [
    [0, 1, 0, 1, 1],
    [1, 0, 1, 0, 0],
    [0, 1, 0, 1, 0],
    [1, 0, 1, 0, 1],
    [1, 0, 0, 1, 0]
]
print('Node 0 and 3 Are Adjacent? ',are_nodes_adjacent(adj_matrix, 0, 3))  # True
print('Node 1 and 4 Are Adjacent? ',are_nodes_adjacent(adj_matrix, 1, 4))  # False