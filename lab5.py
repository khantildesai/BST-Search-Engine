import time

class Node:
    def __init__(self, data, left = None, right = None):
        self.data = data
        self.left = left
        self.right = right
    
    def __str__(self):
        return self.data
    
class BinarySearchTree:
    def __init__(self, root):
        self.root = root
    
    def insert(self, node):
        inserted = False
        current = self.root
        #print(type(current.data))
        #print(type(node.data))
        while not inserted: 
            if current.data <= node.data:
                if current.left == None:
                    current.left = node
                    inserted = True
                else:
                    current = current.left
            
            if current.data > node.data:
                if current.right == None:
                    current.right = node
                    inserted = True
                else:
                    current = current.right
    
    def search(self, val):
        current = self.root
        searching = True
        start_time = time.time()
        while searching:
            if current.data < val:
                if current.left == None:
                    searching = False
                    return False
            
                else:
                    current = current.left
           
            elif current.data > val:
                if current.false == None:
                    searching = False
                    return False
                else:
                    current = current.right                
             
            else:
                searching = False
                return True
        
        end_time = time.time()
        elapsed = end_time - start_time
        print("time elapsed is" + elapsed)

def constructBST(file_name):
    text = open(file_name, 'r')
    root_node = Node(text.readline())
    result = BinarySearchTree(root_node)
    first = text.read(0)
    for line in text:
        if line == first:
            pass
        else:
           current_node = Node(line)
           result.insert(current_node)
    return result

if __name__ == "__main__":
    constructBST("websites.txt") 
