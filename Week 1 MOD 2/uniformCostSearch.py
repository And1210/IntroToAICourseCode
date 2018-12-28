import BasicTree as bt

#We need a priority queue for USC, similar to a queue however doesnt always follow fifo, rearranged by a certain value
class PriorQueue:
    def __init__(self):
        self.q = []
        
    def enqueue(self, node):
        index = 0 #this queue is arranged so lowest cost has priority (is closer the front)
        while (index < len(self.q) and self.q[index].cost < node.cost): #lets loop through the q to find the location of our node to be inserted
            index = index + 1
        self.q.insert(index, node) #insert the node at this position

    def dequeue(self):
        if (len(self.q) > 0): #if there is something on the queue...
            out = self.q[0] #save the node to a variable
            del self.q[0] #delete it from the q
            return out #return the node
        else: #return None if there is nothing in the queue
            return None

    #finds the index of a node in the queue, returns -1 if not found
    def find(self, node):
        for i in range(0, len(self.q)):
            if (self.q[i].data == node and self.q[i].cost > node.cost):
                return i
        return -1

    # replaces the node at a certain index
    def replace(self, node, index):
        self.q[index] = node

#The Uniform Cost Search function
#tree ----- the tree to search in, must be from the BasicTree library
#val ----- the value being searched for
#returns the cost to get to that value
def UCS(tree, val):
    node = tree.root #current node will start as the tree root
    frontier = PriorQueue() #create a priority queue
    frontier.enqueue(node) #enqueue the root
    explored = [] #the explored list
    while(True): #infinite loop to be broken when returned
        node = frontier.dequeue() #get the lowest cost node from the queue
        if (node == None): #if there was nothing in there, the val wasnt found
            return None
        if (node.data == val): #if there is a match return the node
            return node.cost
        explored.append(node) #this will only be reached if there was no match, add current node to explored
        for n in node.children: #check children of node
            if ((n not in explored) and (n not in frontier.q)): #if the current child isn't explored or in the frontier...
                n.cost = n.cost + node.cost #update the cost of the node (as going through node paths will add the cost)
                frontier.enqueue(n) #add the node to the frontier
            else: #otherwise it is either explored or in the frontier
                index = frontier.contains(n.data) #see if its value is in the frontier
                if (index != -1): #if the child's value is in the frontier
                    frontier.replace(n, index) #replace the node at that index with the current child as it will be lower cost

                
tree = bt.Tree() #create the tree
tree.createTree(4) #populate the tree with 4 layers of random nodes
tree.printTree() #print to console
print()
print("Path to 'A': " + str(UCS(tree, 'A')))
print("Path to 'F': " + str(UCS(tree, 'F')))
print("Path to 'X': " + str(UCS(tree, 'X')))
print("Path to 'Z': " + str(UCS(tree, 'Z')))



