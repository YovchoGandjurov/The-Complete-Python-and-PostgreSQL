class Node:

    def __init__(self, text):
        self.text = text
        self.__next = None

    def set_next(self, node):
        if isinstance(node, Node) or node is None:
            self.__next = node
        else:
            raise TypeError("The 'next' node must be of type Node or None.")

    def get_next(self):
        return self.__next

    def print_details(self):
        print("{}".format(self.text))
