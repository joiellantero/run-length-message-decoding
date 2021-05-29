import math


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def display(head):
    current = head
    # print('encoded message (linked list form):')
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
    # display(head)
    return head


def round_half_up(n, decimals=0):
    multiplier = 10 ** decimals
    return int(math.floor(n * multiplier + 0.5) / multiplier)


def decode(com_msg, head):
    parent = head
    uncom_msg = ""
    res = []

    while (parent != None):
        temp = parent.data
        if temp.isdigit():
            char = parent.next
            for i in range(0, int(temp)-1):
                uncom_msg += char.data
        else:
            uncom_msg += temp
        parent = parent.next

    # print(len(uncom_msg)/len(com_msg), com_msg, '-> ', uncom_msg)
    c = round_half_up(len(uncom_msg)/len(com_msg))
    res.append(uncom_msg)
    res.append(c)
    # print('decoded message (string form):')
    return res


if __name__ == '__main__':
    n = int(input())
    enc_list = []
    for i in range(n):
        enc_list.append(input())
    for item in enc_list:
        res = decode(item, generate_linked_list(item))
        print(res[1], res[0])
