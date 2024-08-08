class Node:
    """Класс для узла списка"""

    def __init__(self, data, next_node=None):
        """
        Конструктор класса Node

        :param data: данные, которые будут храниться в узле
        """
        self.data = data
        self.next_node = next_node


class LinkedList:
    """Класс для односвязного списка"""
    def __init__(self):
        self.head = self.tail = None

    def insert_beginning(self, data: dict) -> None:
        """Принимает данные (словарь) и добавляет узел с этими данными в начало связанного списка"""
        new_obj = Node(data)
        if not self.head:
            self.head = self.tail = new_obj
        else:
            s = self.head
            self.head = new_obj
            new_obj.next_node = s

    def insert_at_end(self, data: dict) -> None:
        """Принимает данные (словарь) и добавляет узел с этими данными в конец связанного списка"""
        new_obj = Node(data)
        if not self.tail:
            self.head = self.tail = new_obj
        else:
            self.tail.next_node = new_obj
            self.tail = new_obj

    def __str__(self) -> str:
        """Вывод данных односвязного списка в строковом представлении"""
        node = self.head
        if node is None:
            return str(None)

        ll_string = ''
        while node:
            ll_string += f' {str(node.data)} ->'
            node = node.next_node

        ll_string += ' None'
        return ll_string

    def to_list(self):
        lst = []
        h = self.head
        while h:
            lst.append(h.data)
            h = h.next_node

        return lst

    @staticmethod
    def __check_id(id):
        if type(id) != int:
            raise TypeError

    def get_data_by_id(self, id):
        try:
            self.__check_id(id)
            lst = self.to_list()
            for key in lst:
                if key['id'] == id:
                    return key
        except TypeError:
            return F"Данные не являются словарем или в словаре нет id."
