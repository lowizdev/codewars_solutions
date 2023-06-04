def loop_size(node):
    node_cache = {}
    index = 0
    while(True): # would be better if there was a boolean variable to control, and also, it could have a max_iteration flag
        if node in node_cache: 
            return index - node_cache[node]
        node_cache[node] = index
        node = node.next
        index += 1