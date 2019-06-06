from linkedlist import LinkedList


class LinkedQueue:

    def __init__(self):
        self.__linked_list = LinkedList()

    def push(self, node):
        self.__linked_list.add_start_to_list(node)

    def pop(self):
        return self.__linked_list.remove_end_from_list()

    def find(self, name):
        return self.__linked_list.find(name)

    def print_details(self):
        self.__linked_list.print_list()

    def __len__(self):
        return self.__linked_list.size()
