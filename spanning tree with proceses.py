from multiprocessing import Process
import multiprocessing
import time


def function1():
    for i in range(5):
        time.sleep(1)


def function2():
    for i in range(5):
        time.sleep(1)


def function3():
    for i in range(5):
        time.sleep(1)


def function4():
    for i in range(5):
        time.sleep(1)


def function5():
    for i in range(5):
        time.sleep(1)


class Process_creation(Process):
    def __init__(self, value, proc):
        super(Process_creation, self).__init__()
        self.left = None
        self.right = None
        self.process_ID = value
        self.token_color = None
        self.message = None
        if proc.is_alive():
            self.state = 'Active'
        else:
            self.state = 'Idle'
        self.proc = proc


class SpanningTree:
    def createNode(self, ID, proc):
        return Process_creation(ID, proc)

    def add_process(self, node, ID, proc):
        if node is None:
            return self.createNode(ID, proc)

        if node.left is None:
            node.left = self.add_process(node.left, ID, proc)
        elif node.right is None:
            node.right = self.add_process(node.right, ID, proc)

        else:
            if node.left is not None and node.right is not None:
                self.add_process(node.left, ID, proc)
            elif node.right is not None:
                self.add_process(node.right, ID, proc)

        return node

    def Is_Leaf(self, node):
        if node.left is None and node.right is None:
            return True
        else:
            return False

    def print_tree(self, root):
        if root is not None:
            temp = root.token_color
            if temp is None:
                temp = "No Token Revieved"
            print(f'process {root.process_ID}, State : {root.state}, Token : {temp}')
            self.print_tree(root.left)
            self.print_tree(root.right)

    def make_leaf_idle(self, root):
        if root is not None:
            if self.Is_Leaf(root):
                root.state = 'Idle'
                root.token_color = 'White'

            self.make_leaf_idle(root.left)
            self.make_leaf_idle(root.right)

    def make_process_idle(self, root, pid):

        if root is not None:
            if root.process_ID == pid:
                if root.left.state is not None and (root.left.token_color is not None or root.left.token_color == 'White'):
                    if root.right.state is not None and (root.right.token_color is not None or root.right.token_color == 'White'):
                        root.state = 'Idle'
                    else:
                        print(f'Cannot Make process {root.process_ID} Idle its child process is not yet completed')
                        return

            self.make_process_idle(root.left, pid)
            self.make_process_idle(root.right, pid)

    def check_messages(self, root):
        if root is not None:
            if root.message is not None:
                root.token_color = 'Black'
                root.state = 'Active'
                print(f'process {root.process_ID},Message Sent {root.message}, State : {root.state}, Token : {root.token_color}')

            self.check_messages(root.left)
            self.check_messages(root.right)

    def get_tokens(self, root):
        if root is not None:

            if root.left is not None:
                if root.left.token_color == 'White':
                    if root.token_color is None and root.token_color != 'Black':
                        root.token_color = 'White'
                elif root.left.token_color == 'Black':
                    root.token_color = 'Black'

            if root.right is not None:
                if root.right.token_color == 'White':
                    if root.token_color is None and root.token_color != 'Black':
                        root.token_color = 'White'
                elif root.right.token_color == 'Black':
                    root.token_color = 'Black'

            self.get_tokens(root.left)
            self.get_tokens(root.right)

    def Is_all_idle(self, root):
        if root is not None:
            if not root.proc.is_alive():
                pass
            else:
                return 'NO'
            self.Is_all_idle(root.left)
            self.Is_all_idle(root.right)

    def send_message(self, root, pid, msg):
        if root is not None:
            if root.process_ID == pid:
                root.message = msg

            self.send_message(root.left, pid, msg)
            self.send_message(root.right, pid, msg)

    def reset(self, root):
        if root is not None:
            root.state = 'Active'
            root.token_color = None
            root.message = None

            self.reset(root.left)
            self.reset(root.right)

    def check_termination(self, root):
        if root is not None:
            if not root.proc.is_alive():
                pass
            else:
                return 'NO'
            self.check_termination(root.left)
            self.check_termination(root.right)


def add_process_to_tree(tree, root, pid, proc):
    tree.add_process(root, pid, proc)


def make_leaf_idle(tree, root):
    print('____________________________________________________________________________________________________________')
    print('Making Leaf Nodes Idle and set token value...')
    print('____________________________________________________________________________________________________________')
    tree.make_leaf_idle(root)
    tree.print_tree(root)


def send_token_to_parent(tree, root):
    print('____________________________________________________________________________________________________________')
    print('Sending token to parent process and checking for messages...')
    print('____________________________________________________________________________________________________________')
    tree.check_messages(root)
    tree.get_tokens(root)
    tree.print_tree(root)


def send_message(tree, root, pid):
    print('____________________________________________________________________________________________________________')
    print(f'Some process sending message to {pid}...')
    print('____________________________________________________________________________________________________________')
    print(' ')
    tree.send_message(root, pid, "Go Active")
    print(' ')
    tree.check_messages(root)
    while root.token_color != 'Black':
        tree.get_tokens(root)
    tree.print_tree(root)


def reset(tree, root):
    print('____________________________________________________________________________________________________________')
    print('Reset process again..')
    print('____________________________________________________________________________________________________________')
    temp = tree.Is_all_idle(root)
    if root.token_color == 'Black':
        tree.reset(root)
    elif temp == "NO":
        print('Some Processes are still active')
    else:
        print("All process TERMINATED !!")
        return
    tree.print_tree(root)


if __name__ == '__main__':

    root = None
    tree = SpanningTree()
    p = multiprocessing.Process(target=function1)
    p.start()
    root = tree.add_process(root, p.pid, p)

    n = int(input("Enter the Number of Processors you need to create: "))
    list = [function2, function3, function4, function5]
    temp = p.pid
    for i in range(n-1):
        p = multiprocessing.Process(target=list[i])
        p.start()
        add_process_to_tree(tree, root, p.pid, p)
        if i == 3:
            temp = p.pid
    tree.print_tree(root)

    make_leaf_idle(tree, root)
    time.sleep(1)
    send_token_to_parent(tree, root)
    time.sleep(1)
    send_message(tree, root, temp)
    time.sleep(1)
    reset(tree, root)
    time.sleep(1)

    while True:
        if tree.check_termination(root) is None:
            print("ALL PROCESS TERMINATED !!!")
            break
        else:
            print("Checking for Termination")
            time.sleep(1)
