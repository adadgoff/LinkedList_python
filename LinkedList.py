class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


class LinkedList:
    def __init__(self):
        self.head = None
        self.size = 0

    def __str__(self):
        elements_of_linked_list = []
        cur_node = self.head
        while cur_node is not None:
            elements_of_linked_list.append(cur_node.data)
            cur_node = cur_node.next
        return " -> ".join([str(element) for element in elements_of_linked_list]) + "\n"

    def __len__(self):
        return self.size

    def push_front(self, data):
        cur_node = self.head
        new_node = Node(data)
        new_node.next = cur_node
        self.head = new_node
        self.size += 1

    def insert(self, data, index):
        cur_node = self.head
        cur_index = 0
        new_node = Node(data)
        if index > len(self) or index < 0:
            raise Exception("Index out of range")
        if index == 0:
            self.push_front(data)
        else:
            while cur_index + 1 != index:
                cur_node = cur_node.next
                cur_index += 1
            after_cur_node = cur_node.next
            cur_node.next = new_node
            new_node.next = after_cur_node
            self.size += 1

    def append(self, data):  # добавление в конец
        cur_node = self.head
        new_node = Node(data)
        if cur_node is None:  # size = 0
            self.head = new_node
        else:  # size != 0
            while cur_node.next is not None:
                cur_node = cur_node.next
            cur_node.next = new_node
        self.size += 1

    def remove_front(self):
        cur_node = self.head
        self.head = cur_node.next
        self.size -= 1

    def remove(self, index):
        cur_node = self.head
        cur_index = 0
        if index >= len(self) or index < 0:
            raise Exception("Index out of range")
        if index == 0:
            self.remove_front()
        else:
            while cur_index + 1 != index:
                cur_node = cur_node.next
                cur_index += 1
            remove_node = cur_node.next
            after_remove_node = remove_node.next
            cur_node.next = after_remove_node
            self.size -= 1

    def remove_back(self):
        cur_node = self.head
        while cur_node.next.next is not None:
            cur_node = cur_node.next
        cur_node.next = None
        self.size -= 1

    def value_at(self, index):
        cur_node = self.head
        cur_index = 0
        if index >= len(self) or index < 0:
            raise Exception("Index out of range")
        while cur_node is not None:
            if cur_index == index:
                return cur_node.data
            cur_index += 1
            cur_node = cur_node.next

    def reverse(self):
        prev = None
        cur_node = self.head
        next = None
        while cur_node is not None:
            next = cur_node.next
            cur_node.next = prev
            prev = cur_node
            cur_node = next
        self.head = prev


if __name__ == "__main__":
    my_list = LinkedList()
    my_list.append(1)
    my_list.append(3)
    my_list.append(5)
    my_list.append(7)
    print(my_list)

    my_list.insert(9, 4)
    print(my_list)

    my_list.reverse()
    print(my_list)

    my_list.remove(4)
    print(my_list)

    print(str(my_list.value_at(3)) + '\n')

    print(len(my_list))
