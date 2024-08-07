class Node:
    """Класс для узла очереди"""

    def __init__(self, data, next_node=None):
        """
        Конструктор класса Node

        :param data: данные, которые будут храниться в узле
        """
        self.data = data
        self.next_node = next_node


class Queue:
    """Класс для очереди"""

    def __init__(self):
        """Конструктор класса Queue"""
        self.head = self.tail = None

    def enqueue(self, data):
        new_node = Node(data)
        """
        Метод для добавления элемента в очередь

        :param data: данные, которые будут добавлены в очередь
        """
        if self.tail:
            self.tail.next_node = new_node
        self.tail = new_node

        if self.head is None:
            self.head = new_node

    def dequeue(self):
        """
        Метод для удаления элемента из очереди. Возвращает данные удаленного элемента

        :return: данные удаленного элемента
        """
        s = self.head
        if self.head is None:
            return

        self.head = self.head.next_node
        if self.head is None:
            self.tail = None

        return s.data

    def __str__(self):
        """Магический метод для строкового представления объекта"""
        lst = []
        h = self.head
        while h:
            lst.append(str(h.data))
            h = h.next_node
        return '\n'.join(lst)

