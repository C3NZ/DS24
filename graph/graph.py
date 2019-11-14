graph = {"A": set(["B"]), "B": set(["C", "D"]), "C": set(["D"]), "D": set()}
queue = []


def bfs(from_node, to_node):
    parents = {from_node: None}
    queue.append(from_node)
    seen_nodes = set()

    while queue:
        curr_node = queue.pop(0)

        if curr_node != to_node:
            connected_nodes = list(graph[curr_node])

            for node in connected_nodes:
                if not node in seen_nodes:
                    parents[node] = curr_node
                    seen_nodes.add(node)
                    queue.append(node)
        else:
            path = []
            while curr_node is not None:
                path.insert(0, curr_node)
                curr_node = parents[curr_node]
            return path


print(bfs("A", "D"))
