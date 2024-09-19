from binarytree import Node
from binarytree import build


root = Node(3)
root.left = Node(6)
root.left.right=Node(8)
root.left.left=Node(90)
root.right = Node(8)
root.right.left=Node(12)
root.right.right=Node(13)

print('height of tree is :',root.height)
# Getting binary tree
print('Binary tree :', root)
print('Size of our tree is',root.size)
# Getting list of nodes
print('List of nodes :', list(root))
# Getting inorder of nodes
print('Inorder of nodes :', root.inorder)
print('postorder of nodes are:',root.postorder)
print('pre order:',root.preorder)

from collections import deque


# BFS from given source s
def bfs(adj, s, visited):
    # Create a queue for BFS
    q = deque()

    # Mark the source node as visited and enqueue it
    visited[s] = True
    q.append(s)

    # Iterate over the queue
    while q:

        # Dequeue a vertex from queue and print it
        curr = q.popleft()
        print(curr, end=" ")

        # Get all adjacent vertices of the dequeued
        # vertex. If an adjacent has not been visited,
        # mark it visited and enqueue it
        for x in adj[curr]:
            if not visited[x]:
                visited[x] = True
                q.append(x)


# Function to add an edge to the graph
def add_edge(adj, u, v):
    adj[u].append(v)
    adj[v].append(u)


# Example usage
if __name__ == "__main__":
    # Number of vertices in the graph
    V = 5

    # Adjacency list representation of the graph
    adj = [[] for _ in range(V)]

    # Add edges to the graph
    add_edge(adj, 0, 1)
    add_edge(adj, 0, 2)
    add_edge(adj, 1, 3)
    add_edge(adj, 1, 4)
    add_edge(adj, 2, 4)

    # Mark all the vertices as not visited
    visited = [False] * V

    # Perform BFS traversal starting from vertex 0
    print("BFS starting from 0: ")
    bfs(adj, 0, visited)


##Bfs trversel code

from binarytree import Node

# Create the binary tree
root = Node(5)
root.left = Node(3)
root.right = Node(6)
root.left.left = Node(1)
root.left.right = Node(2)

def bfs(node):
    if not node:
        return []

    queue = [node]  # Initialize the queue with the root node
    result = []

    while queue:
        current = queue.pop(0)  # Dequeue the front node
        result.append(current.value)  # Process the current node

        # Enqueue left and right children if they exist
        if current.left:
            queue.append(current.left)
        if current.right:
            queue.append(current.right)

    return result

# Print the binary tree structure
print("Binary Tree Structure:\n", root)

# Perform BFS and print the result
print("BFS Traversal:", bfs(root))

from binarytree import Node
from collections import deque

from pygame.mixer_music import queue

# Create the binary tree
root = Node(5)
root.left = Node(3)
root.right = Node(6)
root.left.left = Node(1)
root.left.right = Node(2)
print(root)

def BFS(root):
    queue=[root]
    result=[]
    while queue:
        current=queue.pop(0)
        result.append(current.value)
        if current.left:
            queue.append(current.left)
        if current.right:
            queue.append(current.right)
        return result

print(root.levelorder)











