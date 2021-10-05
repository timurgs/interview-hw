class Stack:

    def __init__(self, stack):
        self.stack = stack

    def is_empty(self):
        if len(self.stack) == 0:
            return True
        else:
            return False

    def push(self, element):
        self.stack.append(element)

    def pop(self):
        self.stack.pop()
        if len(self.stack) != 0:
            return self.stack[-1]

    def peek(self):
        return self.stack[-1]

    def size(self):
        return len(self.stack)


def is_balanced(text):
    opening = '[({'
    closing = '])}'
    stack = []
    balance = Stack(stack)
    for i in text:
        if i in opening:
            balance.push(opening.index(i))
        elif i in closing:
            if balance.is_empty() is False and balance.peek() == closing.index(i):
                balance.pop()
            else:
                return 'Несбалансированно'
    if balance.size() == 0:
        return 'Сбалансированно'
    else:
        return 'Несбалансированно'


if __name__ == '__main__':
    check = is_balanced('[([])((([[[]]])))]{()}')
    print(check)
