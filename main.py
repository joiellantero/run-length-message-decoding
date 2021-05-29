class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def display(head):
    current = head
    print('encoded message (linked list form):')
    while current is not None:
        print(current.data, end=" -> ")
        current = current.next
    print('\n')


def generate_linked_list(text):
    def add(data):
        temp = Node(data)
        temp.next = None
        return temp

    def converter(text, head):
        head = add(text[0])
        current = head

        for j in range(len(text) - 1):
            temp = text[j + 1]
            if current.data.isdigit() and ord(temp) >= ord('0') and ord(temp) <= ord('9'):
                current.data += text[j + 1]
            else:
                current.next = add(text[j + 1])
                current = current.next

        return head

    head = None
    head = converter(text, head)
    display(head)
    return head


def decode(head):
    parent = head
    res = ""

    while (parent != None):
        count = 0
        temp = parent.data
        if temp.isdigit():
            char = parent.next
            for i in range(0, int(temp)-1):
                res += char.data
        else:
            res += temp
        parent = parent.next

    print('decoded message (string form):')
    return res

if __name__ == '__main__':
    n = int(input())
    enc_list = []
    for i in range(n):
        enc_list.append(input())
    for item in enc_list:
        print(decode(generate_linked_list(item)))
