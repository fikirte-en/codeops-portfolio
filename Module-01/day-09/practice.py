# %%
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def insert(root, value):
    if root is None:
        return Node(value)   # base case: empty spot found, create the node here
    if value < root.value:
        root.left = insert(root.left, value)
    else:
        root.right = insert(root.right, value)
    return root


def in_order(root, result=None):
    if result is None:
        result = []
    if root is not None:
        in_order(root.left, result)    
        result.append(root.value)      
        in_order(root.right, result)  
    return result


root = None
for balance in [500, 200, 800, 100, 300, 700, 900]:
    root = insert(root, balance)

print(in_order(root))  
# %%
def height(node):
    if node is None:
        return 0   
    left_height = height(node.left)
    right_height = height(node.right)
    return 1 + max(left_height, right_height)


print(height(root))
# %%
def dfs(graph, start, visited=None):
    if visited is None:
        visited = set()
    visited.add(start)
    for neighbor in graph.get(start, []):
        if neighbor not in visited:
            dfs(graph, neighbor, visited)
    return visited


print(dfs(graph, "A"))
# %%
def dfs_ordered(graph, start, visited=None, order=None):
    if visited is None:
        visited = set()
        order = []
    visited.add(start)
    order.append(start)
    for neighbor in graph.get(start, []):
        if neighbor not in visited:
            dfs_ordered(graph, neighbor, visited, order)
    return order


print("BFS-style queue order would visit: A, B, C, D, E (roughly, by layer)")
print("DFS visit order:", dfs_ordered(graph, "A"))
# %%
import heapq

tasks = []
heapq.heappush(tasks, (3, "Write report"))
heapq.heappush(tasks, (1, "Fix critical bug"))
heapq.heappush(tasks, (2, "Review PR"))
heapq.heappush(tasks, (5, "Update docs"))
heapq.heappush(tasks, (1, "Handle outage"))

while tasks:
    priority, task = heapq.heappop(tasks)
    print(f"Priority {priority}: {task}")
# %%
