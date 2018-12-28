import BasicTree as bt #import the basic tree library

#The main depth-first search function, it calls a helper function with the correct parameters
#tree ----- the BasicTree tree variable setup beforehand, this is what will be searched (could also be called the state space)
#val ----- the value to search for
#This will return a string which is the path needed to take to get to val
def DFS(tree, val):
    return DFSRecursive(tree.root, tree.layers, val)

#This is what's known as a recursive helper function, it will do the heavy lifting of the algorithm
def DFSRecursive(node, numLayers, val):
    #remember, every bit of code here will be run for every node called, not just the root one
    
    if (node.data == val): #if we have reached a node with data equal to the val...
        return str(node.data) #return the data as a string
    elif (numLayers <= 0): #if we have exhausted all layers...
        return None #return None type, this means the val wasn't found
    else: #otherwise...
        cutoff = False #initialize a cutoff variable, this will be used to flag if all children are leaf nodes and don't contain our desired val
        for n in node.children: #for every child...
            result = DFSRecursive(n, numLayers-1, val) #the result for every child should be the result of it's children (this is where the recursion happens)
            if (result == None): #if the result is None, we have reached the end layer
                cutoff = True #flag with the cutoff variable
            else: #otherwise we have found a matching node!
                return str(node.data) + '->' + result #return the current node's data val with the result (this node must lead to the solution)
        if (cutoff): #if we hit a cutoff...
            return None #return None
        
tree = bt.Tree() #create the tree
tree.createTree(4) #populate the tree with 4 layers of random nodes
tree.printTree() #print to console
print()
print("Path to 'A': " + str(DFS(tree, 'A')))
print("Path to 'F': " + str(DFS(tree, 'F')))
print("Path to 'X': " + str(DFS(tree, 'X')))
print("Path to 'Z': " + str(DFS(tree, 'Z')))
