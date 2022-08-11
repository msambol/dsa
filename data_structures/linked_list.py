class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

    def __str__(self):
        return str(self.data)
 

class LinkedList:
    def __init__(self):
        self.head = None

    # O(n)
    def search(self, target):
        current = self.head
        while current:
            if current.data == target:
                return current 
            current = current.next
        return None

    # O(1)
    def insert(self, node):
        node.next = self.head
        if self.head:
            self.head.prev = node

        self.head = node
        node.prev = None

    # O(1)
    def delete(self, node):
        if node.prev is not None:
            node.prev.next = node.next
        else:
            self.head = node.next
        
        if node.next is not None:
            node.next.prev = node.prev

    def print_list(list):
        current = list.head
        while current:
            print(f'{current.data} -->', end=' ')
            current = current.next

        print('None')
                

def main():
    ll = LinkedList()
    ll.print_list()

    ll.insert(Node(5))
    ll.print_list()

    ll.insert(Node(4))
    ll.insert(Node(3))
    ll.insert(Node(2))
    ll.insert(Node(1))
    ll.print_list()

    node_to_delete = ll.search(4)
    print(f'Deleting {node_to_delete}..')
    ll.delete(node_to_delete)
    ll.print_list()

    node_to_delete = ll.search(2)
    print(f'Deleting {node_to_delete}..')
    ll.delete(node_to_delete)
    ll.print_list()

    print(ll.search(3))
    print(ll.search(99))

main()
