class Node:

    def __init__(self, data, value):
        self.data = data
        self.value = value
        self.__left = None
        self.__right = None

    def set_right(self, node):
        if isinstance(node, Node) or node is None:
            self.__right = node
        else:
            raise TypeError("The 'right' node must be of type Node or None.")

    def set_left(self, node):
        if isinstance(node, Node) or node is None:
            self.__left = node
        else:
            raise TypeError("The 'left' node must be of type Node or None.")

    def get_right(self):
        return self.__right

    def get_left(self):
        return self.__left

    def print_details(self):
        print("{}: {}".format(self.value, self.data))
