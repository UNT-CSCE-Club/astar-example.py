from numpy import array as vector
from Node import Node
from Heap import Heap

#Variables
maxX, maxY = 10, 10 #Size of grid
startNodePos = vector([1,1])
targetNodePos = vector([8,9])

#Construct Nodes
Nodes = [] #maxX x maxY matrix

for i in range(maxX):
    NodeColumn = []
    Nodes.insert(i, NodeColumn)
    for j in range(maxY):
        newNode = Node(vector([i, j]))
        newNode.Neighbors = newNode.GetNeighbors(maxX, maxY)
        NodeColumn.insert(j, newNode)
        
#Initiation
open = Heap() #Nodes to be evalued
closed = [] #Nodes already evaluated

startNode = Nodes[startNodePos[0]][startNodePos[1]]
startNode.Traversable = True
startNode.n = 0

targetNode = Nodes[targetNodePos[0]][targetNodePos[1]]
targetNode.Traversable = True

current = startNode
open.Append(startNode)

while not (current == targetNode):
    current = open.arr[0]
    open.Remove(current)
    closed.append(current)

    #Loop neighbors
    for NeighborPos in current.Neighbors:
        Neighbor = Nodes[NeighborPos[0]][NeighborPos[1]]

        

        break

    break
