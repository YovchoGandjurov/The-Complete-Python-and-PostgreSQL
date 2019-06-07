from unittest import TestCase
from node import Node
from linkedlist import LinkedList
from linkedstack import LinkedStack


class TestLinkedList(TestCase):
    """
    This class tests that your LinkedList class was implemented
    correctly.
    """

    def test_node_creation(self):
        name = "Jose"

        node = Node(name)

        self.assertEqual(name, node.text)

    def test_list_creation(self):
        linked_list = LinkedList()

        self.assertIsNone(linked_list.get_root())

    def test_add_to_list_start(self):
        name = "Jose"

        node = Node(name)

        linked_list = LinkedList()

        linked_list.add_start_to_list(node)

        self.assertEqual(linked_list.get_root(), node)

    def test_add_many_to_list_start(self):
        names = ("Jose", "Rolf", "Anna")

        nodes = [Node(name) for name in names]

        linked_list = LinkedList()

        for node in nodes:
            linked_list.add_start_to_list(node)

        marker = linked_list.get_root()
        for i in range(len(nodes)-1, -1, -1):
            self.assertEqual(marker, nodes[i])
            marker = marker.get_next()

    def test_remove_start_from_list(self):
        names = ("Jose", "Rolf", "Anna")

        nodes = [Node(name) for name in names]

        linked_list = LinkedList()

        for node in nodes:
            linked_list.add_start_to_list(node)

        self.assertIsNotNone(linked_list.find("Jose"))

        popped_node = linked_list.remove_start_from_list()

        self.assertEqual(popped_node, nodes[len(nodes) - 1])

        with self.assertRaises(LookupError):
            linked_list.find("Anna")

    def test_find_in_list(self):
        names = ("Jose", "Rolf", "Anna")

        nodes = [Node(name) for name in names]

        linked_list = LinkedList()

        for node in nodes:
            linked_list.add_start_to_list(node)

        marker = linked_list.get_root()
        for i in range(len(nodes) - 1, -1, -1):
            self.assertEqual(linked_list.find(marker.text), nodes[i])
            marker = marker.get_next()

    def test_find_missing_in_list(self):
        linked_list = LinkedList()

        with self.assertRaises(LookupError):
            linked_list.find("Smith")


class TestStack(TestCase):
    def test_push_to_stack(self):
        name = "Jose"

        node = Node(name)
        stack = LinkedStack()

        stack.push(node)

        self.assertEqual(len(stack), 1)

    def test_pop_from_stack(self):
        name = "Jose"

        node = Node(name)
        stack = LinkedStack()

        stack.push(node)

        self.assertEqual(len(stack), 1)

        popped = stack.pop()

        self.assertEqual(popped, node)
        self.assertEqual(len(stack), 0)
