from unittest import TestCase
from node import Node
from linkedlist import LinkedList
from linkedqueue import LinkedQueue


class TestLinkedList(TestCase):

    def test_node_creation(self):
        name = "Jose"
        phone = "123-456-7890"

        node = Node(name, phone)

        self.assertEqual(name, node.name)
        self.assertEqual(phone, node.phone)

    def test_list_creation(self):
        linked_list = LinkedList()

        self.assertIsNone(linked_list.get_root())

    def test_add_to_list_start(self):
        name = "Jose"
        phone = "123-456-7890"

        node = Node(name, phone)

        linked_list = LinkedList()

        linked_list.add_start_to_list(node)

        self.assertEqual(linked_list.get_root(), node)

    def test_add_many_to_list_start(self):
        names = ("Jose", "1234-356"), ("Rolf", "2345-1-53563-2"), ("Anna", "345623-16779-3")

        nodes = [Node(name, phone) for name, phone in names]

        linked_list = LinkedList()

        for node in nodes:
            linked_list.add_start_to_list(node)

        marker = linked_list.get_root()
        for i in range(len(nodes)-1, -1, -1):
            self.assertEqual(marker, nodes[i])
            marker = marker.get_next()

    def test_remove_end_from_list(self):
        names = ("Jose", "1234-356"), ("Rolf", "2345-1-53563-2"), ("Anna", "345623-16779-3")

        nodes = [Node(name, phone) for name, phone in names]

        linked_list = LinkedList()

        for node in nodes:
            linked_list.add_start_to_list(node)

        self.assertIsNotNone(linked_list.find("Jose"))

        popped_node = linked_list.remove_end_from_list()

        self.assertEqual(popped_node, nodes[0])

        with self.assertRaises(LookupError):
            linked_list.find("Jose")

    def test_find_in_list(self):
        names = ("Jose", "1234-356"), ("Rolf", "2345-1-53563-2"), ("Anna", "345623-16779-3")

        nodes = [Node(name, phone) for name, phone in names]

        linked_list = LinkedList()

        for node in nodes:
            linked_list.add_start_to_list(node)

        marker = linked_list.get_root()
        for i in range(len(nodes) - 1, -1, -1):
            self.assertEqual(linked_list.find(marker.name), nodes[i])
            marker = marker.get_next()

    def test_find_missing_in_list(self):
        linked_list = LinkedList()

        with self.assertRaises(LookupError):
            linked_list.find("Smith")


class TestQueue(TestCase):
    def test_push_to_queue(self):
        name = "Jose"
        phone = "123-456-7890"

        node = Node(name, phone)
        queue = LinkedQueue()

        queue.push(node)

        self.assertEqual(len(queue), 1)

    def test_pop_from_queue(self):
        name = "Jose"
        phone = "123-456-7890"

        node = Node(name, phone)
        queue = LinkedQueue()

        queue.push(node)

        self.assertEqual(len(queue), 1)

        popped = queue.pop()

        self.assertEqual(popped, node)
        self.assertEqual(len(queue), 0)

    def test_find_in_queue(self):
        name = "Jose"
        phone = "123-456-7890"

        node = Node(name, phone)
        queue = LinkedQueue()

        queue.push(node)

        self.assertEqual(queue.find(name), node)
