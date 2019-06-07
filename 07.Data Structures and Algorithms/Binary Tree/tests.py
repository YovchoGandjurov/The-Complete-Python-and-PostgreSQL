from unittest import TestCase
from node import Node
from binary_tree import BinaryTree


class TestBinaryTree(TestCase):

    def test_node_creation(self):
        name = "Jose"
        value = 1

        node = Node(name, value)

        self.assertEqual(name, node.data)
        self.assertEqual(value, node.value)

    def test_tree_creation(self):
        binary_tree = BinaryTree()

        self.assertIsNone(binary_tree.get_root())

    def test_add_to_tree(self):
        name = "Jose"
        value = 1

        node = Node(name, value)

        binary_tree = BinaryTree()

        binary_tree.add(node)

        self.assertEqual(binary_tree.get_root(), node)

    def test_add_many_to_tree(self):
        names = (("Jose", 2), ("Rolf", 1), ("Anna", 3))

        nodes = [Node(name, value) for name, value in names]

        binary_tree = BinaryTree()

        for node in nodes:
            binary_tree.add(node)

        self.assertEqual(binary_tree.get_root(), nodes[0])
        self.assertEqual(binary_tree.get_root().get_left(), nodes[1])
        self.assertEqual(binary_tree.get_root().get_right(), nodes[2])

    def test_find_in_tree(self):
        names = (("Jose", 2), ("Rolf", 1), ("Anna", 3))

        nodes = [Node(name, value) for name, value in names]

        binary_tree = BinaryTree()

        for node in nodes:
            binary_tree.add(node)

        for i in range(0, len(nodes)):
            self.assertEqual(binary_tree.find(nodes[i].value), nodes[i])

    def test_find_missing_in_list(self):
        binary_tree = BinaryTree()

        with self.assertRaises(LookupError):
            binary_tree.find(5)
