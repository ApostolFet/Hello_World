from __future__ import annotations

from collections.abc import Iterable
from dataclasses import dataclass
from typing import Generic, Self, SupportsIndex, TypeVar, overload
from operator import index


T = TypeVar("T")


@dataclass
class Node(Generic[T]):
    value: T
    head: Node[T] | None = None
    tail: Node[T] | None = None


class LinkedList(Generic[T]):
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
    6
    >>> list(linked_list)
    [0, 1, 2, 3, 4, 5]

    >>> linked_list.pop_left()
    0
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

    >>> max_len_linked_list = LinkedList([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], maxlen=3)
    >>> list(max_len_linked_list)
    [8, 9, 10]
    >>> max_len_linked_list.append(11)
    >>> list(max_len_linked_list)
    [9, 10, 11]
    >>> max_len_linked_list.append_left(8)
    >>> list(max_len_linked_list)
    [8, 9, 10]

    >>> LinkedList([1, 2, 3], maxlen=-1)
    Traceback (most recent call last):
        ...
    ValueError: maxlen must be non-negative

    get last 10 values from generator:
    >>> list(LinkedList((i for i in range(1001)), maxlen=10))
    [991, 992, 993, 994, 995, 996, 997, 998, 999, 1000]
    """

    def __init__(
        self, iterable: Iterable[T] = tuple(), maxlen: int | None = None
    ) -> None:
        self._head = None
        self._tail = None
        self._len = 0

        if maxlen is not None and maxlen < 0:
            raise ValueError("maxlen must be non-negative")
        self._maxlen = maxlen

        for value in iterable:
            self.append(value)

    def append(self, value: T) -> None:
        new_node = Node(value=value, head=self._tail, tail=None)

        if self._tail is not None:
            self._tail.tail = new_node
        self._tail = new_node

        if self._head is None:
            self._head = self._tail

        self._len += 1
        if self._maxlen is not None and self._len > self._maxlen:
            self.pop_left()

    def append_left(self, value: T) -> None:
        new_node = Node(value=value, head=None, tail=self._head)

        if self._head is not None:
            self._head.head = new_node
        self._head = new_node

        if self._tail is None:
            self._tail = self._head

        self._len += 1

        if self._maxlen is not None and self._len > self._maxlen:
            self.pop()

    def pop(self) -> T:
        if self._tail is None:
            raise IndexError("pop from empty linked list")

        value = self._tail.value

        self._tail = self._tail.head
        if self._tail is not None:
            self._tail.tail = None

        self._len -= 1

        return value

    def pop_left(self) -> T:
        if self._head is None:
            raise IndexError("pop from empty linked list")

        value = self._head.value
        self._head = self._head.tail
        if self._head is not None:
            self._head.head = None

        self._len -= 1
        return value

    def __len__(self) -> int:
        return self._len

    @overload
    def __getitem__(self, i: slice) -> Self: ...
    @overload
    def __getitem__(self, i: SupportsIndex) -> T: ...
    def __getitem__(self, i: slice | SupportsIndex) -> Self | T:
        if isinstance(i, slice):
            return self._get_slice(i)
        return self._get_by_index(i)

    def _get_slice(self, i: slice) -> Self:
        cls = type(self)
        values = []
        for item in range(*i.indices(len(self))):
            try:
                value = self[item]
                values.append(value)
            except IndexError:
                break
        return cls(values)

    def _get_by_index(self, i: SupportsIndex) -> T:
        if self._head is None:
            raise IndexError

        i = index(i)
        if i < 0:
            i = len(self) + i

        current_node = self._head
        current_value = current_node.value

        for _ in range(i):
            if current_node.tail is None:
                raise IndexError("index out of range")
            current_node = current_node.tail
            try:
                current_value = current_node.value
            except AttributeError:
                raise IndexError("index out of range")

        return current_value


if __name__ == "__main__":
    import doctest

    doctest.testmod()
