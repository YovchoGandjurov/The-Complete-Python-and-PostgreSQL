from linkedlist import LinkedList


class LinkedStack:
    """
    This class is a stack wrapper around a LinkedList.
    """

    def __init__(self):
        self.__linked_list = LinkedList()

    def push(self, node):
        self.__linked_list.add_start_to_list(node)

    def pop(self):
        return self.__linked_list.remove_start_from_list()

    def print_details(self):
        self.__linked_list.print_list()

    def __len__(self):
        return self.__linked_list.size()
