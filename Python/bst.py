class Node():
    def  __init__(self,
                  key        = None,
                  keycount   = None,
                  leftchild  = None,
                  rightchild = None):
        self.key        = key
        self.keycount   = keycount
        self.leftchild  = leftchild
        self.rightchild = rightchild


def insert(root: Node, key: int) -> Node:
    if root is None:
        node = Node(key)
        node.keycount = 1
        return node
    else:
        if root.key == key:
            root.keycount += 1
            return root
        elif key > root.key:
            root.rightchild = insert(root.rightchild, key)
        elif key < root.key:
            root.leftchild = insert(root.leftchild, key)
    return root

def search_helper(root:Node, search_key: int):
    if root is None or root.key == search_key:
        return root
    
    if search_key < root.key:
        search_helper(root.leftchild, search_key)
        #only when you are traversing
        #you set it equal to left child if you are replaceing the tree
    
    return search_helper(root.rightchild, search_key)

def mininum(root: Node) -> Node:
    if root.leftchild == None:
        return root
    return mininum(root.leftchild)

def delete(root: Node, key: int) -> Node:
    if root is None:
        return root
    
    #traverse to find the key as the "root"
    if root.key > key:
        root.leftchild = delete(root.leftchild, key)
    elif root.key < key:
        root.rightchild = delete(root.rightchild, key)
    else:
        if root is not None: #case where we dont reach the none or end 
            root.keycount -= 1
            if root.keycount == 0: #if root is equal to then go through all four cases
                if root.rightchild is None and root.leftchild is None:
                    root.keycount = 0
                    root = None
                    return root
                
                #case if one children is empty
                elif root.leftchild is None and root.rightchild is not None:
                    root = root.rightchild
                    return root

                elif root.rightchild is None and root.leftchild is not None:
                    root = root.leftchild
                    return root
                
                elif root.key == key:
                    replacement = mininum(root.rightchild)
                    root.key = replacement.key
                    root.keycount = replacement.keycount
                    replacement.keycount = 1
                    root.rightchild = delete(root.rightchild, replacement.key)

    return root

   