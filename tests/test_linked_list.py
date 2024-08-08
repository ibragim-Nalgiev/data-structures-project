"""Здесь надо написать тесты с использованием unittest для модуля linked_list."""
import pytest

from src.linked_list import LinkedList, Node


@pytest.fixture
def linked_list():
    return LinkedList()


def test_node_init():
    node = Node({'id': 1})
    assert node.data == {'id': 1}
    assert node.next_node is None


def test_linked_list_init(linked_list):
    assert linked_list.head is None
    assert linked_list.tail is None


def test_insert_beginning(linked_list):
    linked_list.insert_beginning({'id': 1})
    assert linked_list.head.data == {'id': 1}
    assert linked_list.head.next_node is None
    assert linked_list.tail.data == {'id': 1}

    linked_list.insert_beginning({'id': 0})
    assert linked_list.head.data == {'id': 0}
    assert linked_list.head.next_node.data == {'id': 1}
    assert linked_list.tail.data == {'id': 1}


def test_insert_at_end(linked_list):
    linked_list.insert_at_end({'id': 1})
    assert linked_list.head.data == {'id': 1}
    assert linked_list.head.next_node is None
    assert linked_list.tail.data == {'id': 1}

    linked_list.insert_at_end({'id': 2})
    assert linked_list.head.data == {'id': 1}
    assert linked_list.head.next_node.data == {'id': 2}
    assert linked_list.tail.data == {'id': 2}


def test_str(linked_list):
    assert str(linked_list) == "None"

    linked_list.insert_beginning({'id': 1})
    linked_list.insert_at_end({'id': 2})
    linked_list.insert_at_end({'id': 3})
    linked_list.insert_beginning({'id': 0})

    assert str(linked_list) == " {'id': 0} -> {'id': 1} -> {'id': 2} -> {'id': 3} -> None"


def test_mixed_operations(linked_list):
    linked_list.insert_beginning({'id': 1})
    assert str(linked_list) == " {'id': 1} -> None"

    linked_list.insert_at_end({'id': 2})
    assert str(linked_list) == " {'id': 1} -> {'id': 2} -> None"

    linked_list.insert_beginning({'id': 0})
    assert str(linked_list) == " {'id': 0} -> {'id': 1} -> {'id': 2} -> None"

    linked_list.insert_at_end({'id': 3})
    assert str(linked_list) == " {'id': 0} -> {'id': 1} -> {'id': 2} -> {'id': 3} -> None"


def test_to_list(linked_list):
    assert linked_list.to_list() == []
    linked_list.insert_beginning({'id': 1, 'username': 'lazzy508509'})
    assert linked_list.to_list() == [{'id': 1, 'username': 'lazzy508509'}]
    linked_list.insert_at_end({'id': 2, 'username': 'mik.roz'})
    assert linked_list.to_list() == [{'id': 1, 'username': 'lazzy508509'}, {'id': 2, 'username': 'mik.roz'}]


def test_get_data_by_id(linked_list):
    linked_list.insert_beginning({'id': 1, 'username': 'lazzy508509'})
    linked_list.insert_at_end({'id': 2, 'username': 'mik.roz'})

    # Проверка корректного поиска по id
    assert linked_list.get_data_by_id(1) == {'id': 1, 'username': 'lazzy508509'}
    assert linked_list.get_data_by_id(2) == {'id': 2, 'username': 'mik.roz'}




