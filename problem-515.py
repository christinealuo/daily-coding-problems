# 5 -> 1 -> 8 -> 0 -> 3
# 1 -> 0 -> 5 -> 8 -> 3
# k = 3

# 1 -> 5 -> 8 -> 0 -> 3
# 1 -> 0 -> 5 -> 8 -> 3

# Keep track of the beginning of the linked list
# The most recently encountered number that is smaller than k
# The most recenttly encountered number that is bigger or equal to k

# Runtime: O(N)
# Space complexity: O(1)

class Node: 
    def __init__(self, data): 
        self.data = data 
        self.next = None

class LinkedList: 
    def __init__(self): 
        self.head = None

def problem_515(numbers, k):
    headNode = numbers # 5 -> 1 -> 8 -> 0 -> 3
    setFirstHeadNode = numbers.data < k ? True : False
    currentNode = numbers # 5 -> 1 -> 8 -> 0 -> 3
    lastSmallNode = None
    firstBigNode = None
    while currentNode != None:
        if currentNode.data < k:
            nextNode = currentNode.next # Use to skip over the current node
            if not setFirstHeadNode: # Setting the first head node
                firstBigNode = headNode # Keep track of the first big node (for setting the last small node's next to)
                headNode = currentNode # Setting the new head node to the first small (not necessarily the smallest small)
                headNode.next = firstBigNode
                setFirstHeadNode = True
                lastSmallNode = headNode # Last small node
                currentNode = frstBigNode # Current changes
                previousNode = currentNode # Use to skip over the current node
                currentNode = currentNode.next
            else:
                lastSmallNode.next = currentNode
                lastSmallNode.next.next = firstBigNode
                lastSmallNode = currentNode
                previousNode.next = nextNode # Skip over the node we just moved
                currentNode = nextNode            

