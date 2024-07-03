class Node:
    def __init__(self, numero):
        self.numero = numero
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def insert_node_at_start(self, numero):
        new_node = Node(numero)
        if(self.head is None):
            self.head = new_node
            return
        new_node.next = self.head
        self.head = new_node

    def insert_node_at_end(self, numero):
        new_node = Node(numero)
        if self.head == None:
            self.head = new_node
            return
        current = self.head
        while(current.next):
            current = current.next
        current.next = new_node

    def print_linked_list(self):
        current = self.head
        while current:
            print(current.numero, "->", end=" ")
            current = current.next

    def delete_at_start(self):
        if(self.head is None):
            print("No hay nada que eliminar, lista vacia")
            return
        self.head = self.head.next

    def delete_at_end(self):
        if(self.head is None):
            print("Nada que borrar, la lista esta vacia")
            return

        current = self.head
        while current.next.next:
            current = current.next

        current.next = None


my_list = LinkedList()
my_list.insert_node_at_start("Ana")
my_list.insert_node_at_end(6.2542)
my_list.print_linked_list()
