import copy
import math
from numpy import array as vector

def Magnitude(x):
    return (x**2).sum()**0.5

class Node:
    #A node reprsenting any traversable (or non traversable) square
    def __init__(self, Position):
        self.Position = Position
        self.Traversable = True
        self.GCost = math.inf
        self.HCost = math.inf
        self.FCost = math.inf
        self.Neighbors = []

        #For linked list
        self.Parent = None

        #For heap from open list
        self.n = None #Index in heap
        self.P = None #Parent in heap
        self.L = None #Left child
        self.R = None #Right child
    
    def Clone(self):
        #Clone node
        return copy.copy(self)
    
    def CalcG(self, GCost):
        ParentVector = not (self.Parent is None) and self.Parent.Position
        
        if not (self.Parent is None):
            #Distance from current node to its Parent node
            GCost += Magnitude(self.Position-ParentVector)
  
            #Repeat process for the parent node
            return self.Parent.CalcG(GCost)
        
        return GCost

    def CalcH(self, TargetNode):
        #Distance from self to target node 
        return Magnitude(self.Position-TargetNode.Position)

    def GetNeighbors(self, maxX, maxY):
        Neighbors = []

        for i in range(3):
            for j in range(3):
                x, y = (self.Position[0] + i - 1), (self.Position[1] + j - 1)
                if not (self.Position[0] == x and self.Position[1] == y) and x >= 0 and x <= maxX and y >= 0 and y <= maxY:
                    Neighbors.append(vector([x, y]))
        return Neighbors