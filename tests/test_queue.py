"""Здесь надо написать тесты с использованием unittest для модуля queue."""
import pytest

from src.queue import Queue, Node


@pytest.fixture
def queue1():
    return Queue()


@pytest.fixture
def node1():
    return Node(5, None)


def test_node_init(node1):
    assert node1.data == 5
    assert node1.next_node == None


def test_queue_init(queue1):
    assert queue1.tail == queue1.head == None


def test_enqueue(queue1):
    queue1.enqueue('data1')
    queue1.enqueue('data2')
    queue1.enqueue('data3')
    assert queue1.head.data == 'data1'
    assert queue1.head.next_node.data == 'data2'
    assert queue1.tail.data == 'data3'
    assert queue1.tail.next_node is None
    with pytest.raises(AttributeError):
        print(queue1.tail.next_node.data)


def test_dequeue(queue1):
    queue1.enqueue('data1')
    queue1.enqueue('data2')
    queue1.enqueue('data3')
    queue1.dequeue()
    assert queue1.head.data == 'data2'
    assert queue1.head.next_node.data == 'data3'
    assert queue1.tail.data == 'data3'


def test__str__(queue1):
    queue1.enqueue('data1')
    queue1.enqueue('data2')
    queue1.enqueue('data3')
    assert str(queue1) == "data1\ndata2\ndata3"


def test_dequeue_empty(queue1):
    assert queue1.dequeue() is None


def test_enqueue_after_dequeue(queue1):
    queue1.enqueue('data1')
    queue1.enqueue('data2')
    assert queue1.dequeue().data == 'data1'
    assert queue1.head.data == 'data2'
    assert queue1.tail.data == 'data2'

    queue1.enqueue('data3')
    assert queue1.head.data == 'data2'
    assert queue1.tail.data == 'data3'
    assert queue1.head.next_node.data == 'data3'


def test_mixed_operations(queue1):
    queue1.enqueue('data1')
    assert queue1.dequeue().data == 'data1'
    assert queue1.head is None
    assert queue1.tail is None

    queue1.enqueue('data2')
    assert queue1.head.data == 'data2'
    assert queue1.tail.data == 'data2'

    queue1.enqueue('data3')
    assert queue1.head.data == 'data2'
    assert queue1.tail.data == 'data3'

    assert queue1.dequeue().data == 'data2'
    assert queue1.head.data == 'data3'
    assert queue1.tail.data == 'data3'

    queue1.enqueue('data4')
    assert queue1.head.data == 'data3'
    assert queue1.tail.data == 'data4'
    assert queue1.head.next_node.data == 'data4'
