from __future__ import annotations

from collections.abc import Iterable
from dataclasses import dataclass
from typing import Any, SupportsIndex
from operator import index


@dataclass
class Node:
    value: Any | None
    head: Node | None = None
    tail: Node | None = None


class LinkedList:
    """
    >>> linked_list = LinkedList((1, 2, 3, 4, 5))
    >>> list(linked_list)
    [1, 2, 3, 4, 5]

    >>> linked_list.append(6)
    >>> list(linked_list)
    [1, 2, 3, 4, 5, 6]

    >>> linked_list.append_left(0)
    >>> list(linked_list)
    [0, 1, 2, 3, 4, 5, 6]

    >>> linked_list.pop()
    >>> list(linked_list)
    [0, 1, 2, 3, 4, 5]

    >>> linked_list.pop_left()
    >>> list(linked_list)
    [1, 2, 3, 4, 5]

    >>> 5 in linked_list
    True
    >>> 6 in linked_list
    False

    >>> list(reversed(linked_list))
    [5, 4, 3, 2, 1]

    >>> linked_list[0], linked_list[4]
    (1, 5)

    >>> linked_list[-5], linked_list[-1]
    (1, 5)

    >>> linked_list[100]
    Traceback (most recent call last):
        ...
    IndexError: index out of range

    >>> sliced_linked_list = linked_list[1:4]
    >>> list(sliced_linked_list)
    [2, 3, 4]

    >>> isinstance(sliced_linked_list, LinkedList)
    True

    >>> list(linked_list[:])
    [1, 2, 3, 4, 5]

    >>> list(linked_list[1:-1000])
    []

    >>> list(linked_list[1:1000])
    [2, 3, 4, 5]

    >>> list(linked_list[1:5:2])
    [2, 4]

    >>> empty_linked_list = LinkedList()
    >>> empty_linked_list.pop()
    Traceback (most recent call last):
        ...
    IndexError: pop from empty linked list

    >>> empty_linked_list.pop_left()
    Traceback (most recent call last):
        ...
    IndexError: pop from empty linked list
    """

    def __init__(self, iterable: Iterable = tuple()) -> None:
        self._head = None
        self._tail = None
        self._len = 0

        for value in iterable:
            self.append(value)

    def append(self, value):
        new_node = Node(value=value, head=self._tail, tail=None)

        if self._tail is not None:
            self._tail.tail = new_node
        self._tail = new_node

        if self._head is None:
            self._head = self._tail

        self._len += 1

    def append_left(self, value):
        new_node = Node(value=value, head=None, tail=self._head)

        if self._head is not None:
            self._head.head = new_node
        self._head = new_node

        if self._tail is None:
            self._tail = self._head

        self._len += 1

    def pop(self) -> Any:
        if self._tail is None:
            raise IndexError("pop from empty linked list")

        self._tail = self._tail.head
        if self._tail is not None:
            self._tail.tail = None

        self._len -= 1

    def pop_left(self):
        if self._head is None:
            raise IndexError("pop from empty linked list")
        self._head = self._head.tail
        if self._head is not None:
            self._head.head = None

        self._len -= 1

    def __len__(self) -> int:
        return self._len

    def __getitem__(self, i: SupportsIndex | slice):
        if isinstance(i, slice):
            return self._get_slice(i)
        return self._get_by_index(i)

    def _get_slice(self, i: slice):
        cls = type(self)
        values = []
        for item in range(*i.indices(len(self))):
            try:
                value = self[item]
                values.append(value)
            except IndexError:
                break
        return cls(values)

    def _get_by_index(self, i: SupportsIndex):
        if self._head is None:
            raise IndexError

        i = index(i)
        if i < 0:
            i = len(self) + i

        current_node = self._head
        current_value = current_node.value

        for _ in range(i):
            current_node = current_node.tail
            try:
                current_value = current_node.value
            except AttributeError:
                raise IndexError("index out of range")

        return current_value


if __name__ == "__main__":
    import doctest

    doctest.testmod()
