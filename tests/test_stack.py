"""Здесь надо написать тесты с использованием unittest для модуля stack."""
import pytest

from src.stack import Node, Stack


@pytest.fixture
def stack1():
    return Stack()


@pytest.fixture
def node1():
    return Node(5, None)


def test_node_init(node1):
    assert node1.data == 5
    assert node1.next_node == None


def test_stack_init(stack1):
    assert stack1.top == None


def test_stack_push(stack1):
    stack1.push('data1')
    stack1.push('data2')
    stack1.push('data3')
    assert stack1.top.data == 'data3'


def test_stack_pop(stack1):
    stack1.push('data1')
    stack1.push('data2')
    stack1.push('data3')
    stack1.pop()
    assert stack1.top.data == 'data2'


def test__str__(stack1):
    stack1.push('data1')
    assert str(stack1) == 'data1'



