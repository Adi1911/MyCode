"""
File Name:  morale.py
Author:     Aditya Ajit Tirakannavar (at2650@rit.edu)
Course:     CSCI-665 Foundations of Algorithms
HW 2.5:     Implement an O(mn) algorithm that determines the number of employees at risk, given that there
            are n total employees and m conversational links between employees
            the first line contains a single integer, n, representing the number of employees.
            The second line contains a single integer, m, representing the number of directed communications
            that exist between two employees,
            Following that are m lines. Each line contains three integers separated by spaces.
"""
import math
graph = []

def BellmanFord(V):

    # Initialize distances from Vertex 0 to all other vertices as INFINITE
    distance = [math.inf] * V
    distance[0] = 0

    # Relax all edges N - 1 times to find shortest
    # path from src to any other vertex
    for _ in range(V - 1):
        # Update distance value and parent index of the adjacent vertices of
        # the picked vertex.
        for u, v, w in graph:
            if not distance[u] == math.inf and distance[u] + w < distance[v]:
                distance[v] = distance[u] + w

    # The above step guarantees shortest distances if graph doesn't contain
    # negative weight cycle. If we get a shorter path by doing more than n-1 iterations,
    # then there exists a cycle.
    NegativeCycle = set()
    for u, v, w in graph:
        if not distance[u] == math.inf and distance[u] + w < distance[v]:
            NegativeCycle.add(u)
    if len(NegativeCycle) == 0:
        return 0
    return DFS(NegativeCycle, visited=set())

def DFS( VS, visited):
    for i in VS:
        visited.add(i)
        for a,b,w in graph:
            if b not in visited and a == i and b != None:
                DFS({b}, visited)
    return len(visited)

if __name__ == '__main__':

    V = int(input().strip())
    E = int(input().strip())
    for i in range(E):
        Edg = input().split()
        graph.append([int(Edg[0]), int(Edg[1]), int(Edg[2])])
    print(BellmanFord(V))