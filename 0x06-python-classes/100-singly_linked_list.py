class Node:
    """
    A class representing a node in a singly linked list.

    Attributes:
        data (int): The data value of the node.
        next_node (Node or None): The next node in the linked list or None if it's the last node.
    """

    def __init__(self, data, next_node=None):
        """
        Initializes a new Node with the given data and next_node.

        Args:
            data (int): The data value of the node.
            next_node (Node or None): The next node in the linked list or None if it's the last node.
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """int: The data value of the node."""
        return self._data

    @data.setter
    def data(self, value):
        """
        Setter for the data attribute.

        Args:
            value (int): The new data value.

        Raises:
            TypeError: If the provided value is not an integer.
        """
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self._data = value

    @property
    def next_node(self):
        """Node or None: The next node in the linked list or None if it's the last node."""
        return self._next_node

    @next_node.setter
    def next_node(self, value):
        """
        Setter for the next_node attribute.

        Args:
            value (Node or None): The new next node.

        Raises:
            TypeError: If the provided value is not a Node object or None.
        """
        if value is not None and not isinstance(value, Node):
            raise TypeError("next_node must be a Node object or None")
        self._next_node = value


class SinglyLinkedList:
    """
    A class representing a singly linked list.

    Attributes:
        head (Node or None): The head node of the linked list or None if the list is empty.
    """

    def __init__(self):
        """Initializes an empty SinglyLinkedList."""
        self.head = None

    def sorted_insert(self, value):
        """
        Inserts a new Node into the correct sorted position in the list (increasing order).

        Args:
            value (int): The value of the new node.
        """
        new_node = Node(value)

        # If the list is empty or the new node has a smaller value than the head
        if self.head is None or value < self.head.data:
            new_node.next_node = self.head
            self.head = new_node
            return

        current = self.head
        while current.next_node is not None and current.next_node.data < value:
            current = current.next_node

        new_node.next_node = current.next_node
        current.next_node = new_node

    def __str__(self):
        """
        Returns a string representation of the linked list.

        Returns:
            str: The string representation of the linked list.
        """
        result = []
        current = self.head
        while current:
            result.append(str(current.data))
            current = current.next_node
        return '\n'.join(result)
