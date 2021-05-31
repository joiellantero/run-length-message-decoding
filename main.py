import math


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


# displaying the linked list for testing
def display(head):
    current = head
    while current is not None:
        print(current.data, end=" -> ")
        current = current.next
    print('\n')


# similar to isdigit() or isnumeric() methods
# however, this function extends those methods to be able to check for superscripts and subscripts.
def is_numeric(data):
    count = 0
    for i in data:
        if ord(i) >= ord('0') and ord(i) <= ord('9'):
            continue
        else:
            count += 1
    if count > 0:
        return False
    return True


# we convert the strings into linked list for easier access to the numbers and the unicode characters
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
            # since integers can be two digits or more, I have added this if else statement to address that.
            if is_numeric(current.data) and ord(temp) >= ord('0') and ord(temp) <= ord('9'):
                current.data += text[j + 1]
            else:
                current.next = add(text[j + 1])
                current = current.next

        return head

    head = None
    head = converter(text, head)
    # display(head)
    return head


# Since the current methods in python like round() doesnt round up number like 1.5 or 2.5,
# I added this function which also rounds them up to the nearest whole number.
def round_half_up(n, decimals=0):
    multiplier = 10 ** decimals
    return int(math.floor(n * multiplier + 0.5) / multiplier)


# this function takes in the comprerssed messages by the user and uncompresses it.
def decode(com_msg, head):
    parent = head
    uncom_msg = ""
    res = []

    while (parent != None):
        temp = parent.data
        # if the current node is a digit, we take the next node, repeat it 'temp' times, and append the result to the 'uncom_msg' string variable
        if is_numeric(temp):
            char = parent.next
            for i in range(0, int(temp)-1):
                uncom_msg += char.data

        # if 'temp' is not a number, then we just append it to the uncom_msg since there's no need to repeat it.
        else:
            uncom_msg += temp
        parent = parent.next

    # compute for the compression ratio to check the number of time the data has been reduced.
    c = round_half_up(len(uncom_msg)/len(com_msg))

    # we return both the uncompressed message and the compression ratio to be displayed on the terminal.
    res.append(uncom_msg)
    res.append(c)
    return res


if __name__ == '__main__':
    # obtain the amount of inputs we'll take from the user
    n = int(input())
    enc_list = []

    # obtain the compressed messages from the user
    for i in range(n):
        enc_list.append(input())

    # put the compressed messages into a linked list then pass it to the decode function to be uncompressed
    # linked list was used to separate the integers from the characters for easier access.
    for item in enc_list:
        res = decode(item, generate_linked_list(item))
        print(res[1], res[0])
