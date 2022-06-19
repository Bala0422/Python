'''from collections import deque


class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

    def insert(self, data):
        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)
            elif data > self.data:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)
        else:
            self.data = data

    def PrintTree(self):
        if self.left:
            self.left.PrintTree()
        print(self.data),
        if self.right:
            self.right.PrintTree()

    def mirror(self, v):
        if v is None:
            return
        else:
            self.mirror(v.left)
            self.mirror(v.right)
            temp = v.left
            v.left = v.right
            v.right = temp

    def preorderTraverse(self, root):
        res = []
        if root:
            res.append(root.data)
            res = res + root.preorderTraverse(root.left)
            res = res + root.preorderTraverse(root.right)
        return res

    def postorderTraverse(self, root):
        res = []
        if root:
            res = root.postorderTraverse(root.left)
            res = res + root.postorderTraverse(root.right)
            res.append(root.data)
        return res

    def levelorderTraverse(self, v):
        level = []
        q1 = deque()
        q1.append(v)
        while len(q1) > 0:
            temp = q1.popleft()
            level.append(temp.data)
            if temp.left != None:
                q1.append(temp.left)
            if temp.right != None:
                q1.append(temp.right)
        return level


arraySize = int(input())
arr = list(map(int, input().split()))
if arr[0] > 0:
    root = Node(arr[0])
    for i in range(1, arraySize):
        if arr[i] > 0:
            root.insert(arr[i])
else:
    root = Node(arr[1])
    for i in range(2, arraySize):
        if arr[i] > 0:
            root.insert(arr[i])


post_order = root.postorderTraverse(root)
for i in post_order:
    print(i, end=' ')
print()
before = root.levelorderTraverse(root)
root.mirror(root)
pre_order = root.preorderTraverse(root)
for i in pre_order:
    print(i, end=' ')
after = root.levelorderTraverse(root)

print()
if before == after:
    print("Is a Palindromic Tree")
else:
    print("Is Not a Palindromic Tree")'''


'''
class BinaryTree:
    class node:
        def __init__(self):
            self.element = 0
            self.leftchild = None
            self.rightchild = None
            self.pos = -1
            self.parent = None

    def __init__(self):
        self.sz = 0
        self.root = None
        self.ht = 0

    def insertElement(self, val):
        if self.root is None:
            self.root = self.node()
            self.root.element = val
            self.root.pos = 1
            return
        else:
            newNode = self.node()
            newNode.element = val

            root = self.root
            temp = None

            while root is not None:
                temp = root
                if val < root.element:
                    root = root.leftchild
                else:
                    root = root.rightchild

            if val < temp.element:
                newNode.parent = temp
                temp.leftchild = newNode
                temp.leftchild.pos = temp.pos * 2
            else:
                newNode.parent = temp
                temp.rightchild = newNode
                temp.rightchild.pos = temp.pos * 2 + 1

    def getPercentile(self, val):
        list1 = []
        self.inorderTraverse(self.root, list1)
        length = len(list1)
        index = sorted(list1).index(val)
        length = len(list1)
        return round((100 / length) * (index + 1))

    def hundredPercentile(self, val):
        while val.rightchild is not None:
            val = val.rightchild
        return val.element

    def percGreater(self, val):
        list1 = []
        self.inorderTraverse(self.root, list1)
        length = len(list1)
        j = 0
        for i in range(length):
            if round((100 / length) * (i + 1)) > val:
                j = length - i
                break
        return j

    def inorderTraverse(self, val, list1):
        if val is None:
            return None
        self.inorderTraverse(val.leftchild, list1)
        list1.append(val.element)
        self.inorderTraverse(val.rightchild, list1)

    def preorderTraverse(self, val):
        if val is None:
            return None
        print(val.element, end=' ')
        self.preorderTraverse(val.leftchild)
        self.preorderTraverse(val.rightchild)



tree = BinaryTree()
inp = int(input())
while inp > 0:
    command = input()
    operation = command.split()
    if operation[0] == "I":
        pos = int(operation[1])
        tree.insertElement(pos)
        tree.preorderTraverse(tree.root)
        print()
    elif operation[0] == "P":
        pos = int(operation[1])
        print(tree.getPercentile(pos))
    elif operation[0] == "H":
        print(tree.hundredPercentile(tree.root))
    elif operation[0] == "G":
        pos = int(operation[1])
        print(tree.percGreater(pos))
    inp -= 1

'''


'''class HashTable:
    def __init__(self, size, resolutionMethod):
        self.size = int(size)
        self.slots = [None] * self.size
        self.resolutionMethod = resolutionMethod

    def print(self):
        print(self.slots)

    ## inserts the key, data pair into the table using hashing
    def insert(self, data):
    # @start-editable@
        hash_value = self.hashfunction(data, self.size)
        if self.slots[hash_value] is None:
            self.slots[hash_value] = data
        else:
            new_hash = self.collisionResolutionStrategies(hash_value, self.size, data, -1)
            self.slots[new_hash] = data

    # @end-editable@

    def collisionResolutionStrategies(self, oldhash, size, j, key):
        if self.resolutionMethod == 1:
            return self.linearProbing(oldhash, size, j)
        elif self.resolutionMethod == 2:
            return self.quadraticProbing(oldhash, size, j)
        elif self.resolutionMethod == 3:
            return self.doubleHashing(oldhash, size, j, key)

    def hashfunction(self, key, size):

    # @start-editable@
        return  key % size

    # @end-editable@

    ## this gives the position using linear probing
    def linearProbing(self, oldhash, size, j):

    # @start-editable@

        for i in range(size):
            new_hash = (oldhash + i) % size
            if self.slots[new_hash] is None:
                return new_hash
    # @end-editable@

    def quadraticProbing(self, oldhash, size, j):

    # @start-editable@
        for i in range(1, size):
            new_hash = (oldhash + (i ** 2)) % size
            if self.slots[new_hash] is None:
                return new_hash

    # @end-editable@

    def doubleHashing(self, oldhash, size, j, key):

    # @start-editable@

        def GetPrime():
            for i in range(size, 1, -1):
                Stat = True
                for k in range(2, i):
                    if i % k == 0:
                        Stat = False
                        break
                if Stat:
                    return i
            return -1

        Prime = GetPrime()
        hash1 = oldhash
        hash2 = Prime - (j % Prime)
        for i in range(size):
            hash_value = (hash1 + i * hash2) % size
            if self.slots[hash_value] is None:
                self.slots[hash_value] = j
                return

    # @end-editable@

    ## retrieves the item from the table based on the hashing. Print the starting slot for searching the key, Returns True when key is found and False when the key is not found"
    def search(self, data):

    # @start-editable@

        hash = self.hashfunction(data, self.size)
        if data == self.slots[hash]:
            print(f'start slot  {hash}')
            return True
        else:
            new_hash = self.collisionResolutionStrategies(hash, self.size, data, -1)
            if new_hash == data:
                print(f'start slot  {hash}')
                return True

        return False
    # @end-editable@

    def __getitem__(self, key):
        return self.get(key)

    def __setitem__(self, key, data):
        self.put(key, data)


def testHash():
    collisionResolutionMethod = int(input())
    hashtablesize = int(input())
    H = HashTable(hashtablesize, collisionResolutionMethod)
    inputs = int(input())
    while inputs > 0:
        command = input()
        operation = command.split()
        if (operation[0] == "I"):
            H.insert(int(operation[1]))
        elif (operation[0] == "S"):
            print(H.search(int(operation[1])))
        elif (operation[0] == "P"):
            H.print()
        inputs -= 1


def main():
    testHash()


if __name__ == '__main__':
    main()'''

