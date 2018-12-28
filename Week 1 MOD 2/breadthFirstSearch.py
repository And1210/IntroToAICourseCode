import BasicTree as bt

#This version of breadth first search uses a queue, let's make a simple one
class Queue:
    def __init__(self):
        self.q = []
        
    def enqueue(self, node):
        self.q.append(node) #adds a node to the end of the q

    def dequeue(self):
        if (len(self.q) > 0): #if we have a q with values...
            out = self.q[0] #the node to dequeue is at the front
            del self.q[0] #we have stored the node, delete the front node
            return out #return the node
        else: #if the q has a length of 0
            return None

#The breadth-first search function
#tree ----- the BasicTree variable, what will be searched
#val ----- what is being looked for
#This function will return whether val is in the tree or not
def BFS(tree, val):
    if (tree.root.data == val): #if the root value matches, return it
        return tree.root.data
    frontier = Queue()  #make a queue
    frontier.enqueue(tree.root) #add the root as the starting value in queue
    
    explored = [] #list of already seen nodes
    while (True): #infinite loop that will be broken when we return the function
        node = frontier.dequeue() #dequeue the next node to be worked with
        if (node == None): #if it is None we are at end of queue and therefore didn't find the value
            return 'Not Found'
        explored.append(node) #add current node to explored
        for n in node.children: #for the children of the current node...
            if ((n not in explored) and (n not in frontier.q)): #if the current child is not explored and not in the current queue...
                if (n.data == val): #if the current child matches our value...
                    return 'Found!'
                frontier.enqueue(n) #if the current child doesn't match our value, we add it to the frontier
            
                
tree = bt.Tree() #create the tree
tree.createTree(4) #populate the tree with 4 layers of random nodes
tree.printTree() #print to console
print()
print("Path to 'A': " + str(BFS(tree, 'A')))
print("Path to 'F': " + str(BFS(tree, 'F')))
print("Path to 'X': " + str(BFS(tree, 'X')))
print("Path to 'Z': " + str(BFS(tree, 'Z')))
