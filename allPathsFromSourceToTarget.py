"""
Given a directed acyclic graph (DAG) of n nodes labeled from 0 to n - 1, find all possible paths from node 0 to node n - 1, and return them in any order.

The graph is given as follows: graph[i] is a list of all nodes you can visit from node i (i.e., there is a directed edge from node i to node graph[i][j]).

 
 """
from collections import deque

class Solution:
    """
    Plan:
    1. Translate the problem into graph terms
    vertex - each index in the list [0,1,2,3]
    edges - the list of values in a specified index
    weights - n/a
    
    2. build your graph
    No need for explicit graph, just index properly into the input array to get the neighbors of the current node
    
    3. Traverse the graph
    we need to a traversal, doesnt matter what type
    Use a stack to do a dft on the graph
    keep track of the current path we've taken
    if we find the destination node, append the path we took to the resulting array
    return the resulting array at the end
    """

    # iterative
    # def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]
    #     stack = deque()
    #     stack.append((0, [0])) #node, path to node
    #     res = []
    #     destinationNode = len(graph) - 1
        
    #     while len(stack) > 0:
    #         curr.stack.pop()
    #         currNode, currPath = curr[0], curr[1]
    #         if currNode == destinationNode:
    #             res.append(currPath)
    #         else:
    #             for neighbors in graph(currNode):
    #                 newPath = currPath.copy()
    #                 newPath.append(neighbor)
    #                 stack.append((neightbor, newPath))
    #     return res


    # recursive
    def allPathsSourceTarget(self, graph):
        res = []
        self.allPathsSourceTargetHelper(graph, len(graph) - 1, 0, [0], res)
        return res
    
    def allPathsSourceTargetHelper(self, graph, destinationNode, currNode, currPath, res):
        #base case: if you reach destination node
        if currNode == destinationNode:
            res.append(currPath)
        else:
            for neighbors in graph[currNode]:
                newPath = currPath.copy()
                newPath.append(neighbors)
                self.allPathsSourceTargetHelper(graph, destinationNode, neighbors, newPath, res)


# Input: graph = [[1,2],[3],[3],[]]
# Output: [[0,1,3],[0,2,3]]
# Explanation: There are two paths: 0 -> 1 -> 3 and 0 -> 2 -> 3.
