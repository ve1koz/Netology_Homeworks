class Stack:

    def __init__(self):
        self.stack_obj = []

    def is_empty(self):
        if len(self.stack_obj) == 0:
            print('True')
            return True
        else:
            print('False')
            return False

    def push(self):
        elem = input('Введите элемент стека: ')
        self.stack_obj.append(elem)

    def pop(self):
        print('Элемент стека удален')
        return self.stack_obj.pop(-1)

    def peek(self):
        print(f'Последний элемент стека: {self.stack_obj[-1]}')
        return self.stack_obj[-1]

    def size(self):
        print(f'Длина стека: {len(self.stack_obj)}')
        return len(self.stack_obj)

    commands_dict = {'a': push, 'p': peek, 's': size, 'd': pop, 'e': is_empty}

    def user_command(self):
        y = True
        while y:
            command = input('Введите команду: ').lower()
            if command == 'q':
                y = False
            else:
                self.commands_dict[command](self)


if __name__ == '__main__':
    stack = Stack()
    stack.user_command()