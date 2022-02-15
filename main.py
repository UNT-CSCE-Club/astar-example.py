#2
from numpy import array as vector #X = vector()[0] Y = vector()[1]
from Node import Node
from Heap import Heap

#Variables
maxX, maxY = 10, 10 #Size of grid
startNodePos = vector([1,1]) 
targetNodePos = vector([5,1])

#Construct Nodes
Nodes = [] #maxX maxY 2D matrix

for i in range(maxX):
    NodeColumn = []
    Nodes.insert(i, NodeColumn)
    for j in range(maxY):
        newNode = Node(vector([i, j]))

        #Get neighbors before running the algorithm
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

#Loop
while True:
    current = open.arr[0] #The first node at the start of the heap is the best next node

    if current == targetNode:
        break

    open.Remove() #Removes the node at the start of the heap
    closed.append(current)

    #Loop neighbors
    for neighborPos in current.Neighbors:
        neighbor = Nodes[neighborPos[0]][neighborPos[1]]

        if neighbor.Traversable and not (neighbor in closed):

            #Calculate GCost of alternative path
            neighborClone = neighbor.Clone()
            neighborClone.Parent = current
            newDistance = neighborClone.CalcG() 

            #If alternative path (newDistance) is shorter, or neighbor is not in open
            inOpen = neighbor in open.arr
            if newDistance < neighbor.GCost or not inOpen:
                #Update FCost, then add to Heap
                neighbor.GCost = newDistance
                neighbor.HCost = neighbor.CalcH(targetNode)
                neighbor.FCost = newDistance + neighbor.HCost
                neighbor.Parent = current

                if not inOpen:
                    open.Append(neighbor)

path = current.Trace() 
print(path)