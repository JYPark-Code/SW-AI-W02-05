import sys
input = sys.stdin.readline


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.cursor = None  # 커서 왼쪽 문자

    def append(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            self.tail = new_node
            self.cursor = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
            self.cursor = new_node

    def print_list(self):
        values = []
        current = self.head

        while current:
            values.append(current.data)
            current = current.next

        return "".join(values)


first_letter = input().strip()
ll = LinkedList()

for ch in first_letter:
    ll.append(ch)

cmd_length = int(input())

for _ in range(cmd_length):
    cmd = input().split()

    if cmd[0] == "L":
        if ll.cursor is not None:
            ll.cursor = ll.cursor.prev

    elif cmd[0] == "D":
        if ll.cursor is None:
            ll.cursor = ll.head
        elif ll.cursor.next is not None:
            ll.cursor = ll.cursor.next

    elif cmd[0] == "B":
        if ll.cursor is None:
            continue

        # head 삭제
        if ll.cursor == ll.head:
            deleted = ll.cursor
            ll.head = deleted.next

            if ll.head is not None:
                ll.head.prev = None
            else:
                ll.tail = None  # 리스트가 비면 tail도 None

            ll.cursor = None

        # tail 삭제
        elif ll.cursor == ll.tail:
            deleted = ll.cursor
            ll.tail = deleted.prev
            ll.tail.next = None
            ll.cursor = ll.tail

        # 중간 노드 삭제
        else:
            deleted = ll.cursor
            prev_node = deleted.prev
            next_node = deleted.next

            prev_node.next = next_node
            next_node.prev = prev_node
            ll.cursor = prev_node

    elif cmd[0] == "P":
        new_node = Node(cmd[1])

        # 맨 앞 삽입
        if ll.cursor is None:
            if ll.head is None:
                ll.head = new_node
                ll.tail = new_node
            else:
                new_node.next = ll.head
                ll.head.prev = new_node
                ll.head = new_node

            ll.cursor = new_node

        # 중간 또는 끝 삽입
        else:
            new_node.prev = ll.cursor
            new_node.next = ll.cursor.next

            if ll.cursor.next is not None:
                ll.cursor.next.prev = new_node
            else:
                ll.tail = new_node  # 맨 뒤 삽입이면 tail 갱신

            ll.cursor.next = new_node
            ll.cursor = new_node

print(ll.print_list())