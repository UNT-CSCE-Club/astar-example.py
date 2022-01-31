import math
class Heap:
    def __init__(self):
        self.arr = []

    def Append(self, Node):
        newIndex = len(self.arr)
        self.arr.append(Node)

        Node.n = newIndex
        f, Node.P = math.modf((newIndex-1)/2)
        Node.P = int(Node.P)

        NodeP = self.arr[Node.P]
        
        #If fractional part > 0, right node. else left node
        if abs(f) > .001:
            NodeP.R = newIndex
        else:
            NodeP.L = newIndex
        
        #If Node's FCost is lower than NodeP's Fcost, swap
        while newIndex > 0 and (Node.FCost < NodeP.FCost or (abs(Node.FCost - NodeP.FCost) < .01 and Node.HCost < NodeP.HCost)):
            self.Swap(Node, NodeP)
            NodeP = self.arr[Node.P]
        
    def Remove(self):
        endNode = self.arr[len(self.arr)-1] #Last node
        currentNode = self.arr[0] #First node (node we're removing)

        self.Swap(currentNode, endNode)

        #If we just swapped the same node (startingNode)
        if currentNode.P == endNode.n:
            #Set the L or R child to None
            childNodeKey = currentNode.L == currentNode.n and "L" or currentNode.R == currentNode.n and "R"
            setattr(currentNode, childNodeKey, None)
        
        #Set P's children value to None
        f, PIndex = math.modf((currentNode.n-1)/2)
        PIndex = int(PIndex)
        currentP = self.arr[PIndex]

        if abs(f) > .001:
            currentP.R = None
        else:
            currentP.L = None
                
        
        self.arr.pop(currentNode.n)

        #Compare endNode with its children, and swap with the children with the lowest FCost if it's lower than endNode's FCost
        NodeL, NodeR = endNode.L and self.arr[endNode.L] or None, endNode.R and self.arr[endNode.R] or None
        NodeRCost = not (NodeR is None) and NodeR.FCost or math.inf

        while (not (NodeL is None) and endNode.FCost > NodeL.FCost) or (not (NodeR is None) and endNode.FCost > NodeR.FCost):
            SwapNode = NodeL if not (NodeL is None) and NodeL.FCost < NodeRCost else NodeR
            self.Swap(endNode, SwapNode)

            #Update node
            NodeL = not (endNode.L is None) and self.arr[endNode.L] or None
            NodeR = not (endNode.R is None) and self.arr[endNode.R] or None

            NodeRCost = not (NodeR is None) and NodeR.FCost or math.inf
 
    def Swap(self, Node1, Node2):
        Node3 = Node2.Clone()
        #Swap indexes
        self.arr[Node1.n] = Node2 

        Node2.n = Node1.n
        Node2.P = Node1.P
        Node2.L = Node1.L
        Node2.R = Node1.R

        self.arr[Node3.n] = Node1

        Node1.n = Node3.n
        Node1.P = Node3.P
        Node1.L = Node3.L
        Node1.R = Node3.R