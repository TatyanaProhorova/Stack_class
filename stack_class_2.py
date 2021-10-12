
class Stack(list):

    def __init__(self):
        super().__init__()

    def isEmpty(self):
        """ проверка стека на пустоту. Метод возвращает True или False
        """
        return self == []

    def push(self, last):
        """ добавляет новый элемент на вершину стека. Метод ничего не возвращает
        """
        self.append(last)

    def pop(self, **kwargs):
        """ удаляет верхний элемент стека и возвращает его. Стек меняется.
        """
        return super().pop(-1)
    # def spop(self):
    #     """ удаляет верхний элемент стека и возвращает его. Стек меняется.
    #     """
    #     return self.pop(-1)

    def peek(self):
        """ peek - возвращает верхний элемент стека, но не удаляет его. Стек не меняется
        """
        return self[-1]

    def size(self: list):
        """ возвращает количество элементов в стеке
        """
        return len(self)

# stack = Stack()
# print("это stack", stack)

def try_balance(open_close: str):
    """Программа ожидает на вход строку со скобками. На выход сообщение:
      "Сбалансированно", если строка корректная, и "Несбалансированно", если строка составлена неверно.
    Строка пробелов без скобок - сбалансированная.
    """
    result = f"Cбалансированно"
    open_close_list = list(open_close.replace(" ", ""))
    if len(open_close) % 2 == 1:
        result = f"Несбалансированно"
    else:
        stack = Stack()
        while open_close_list:
            last_item = open_close_list.pop()
            if last_item in "])}":
                stack.push(last_item)
            elif (last_item in "[({") & stack.isEmpty():
                result = f"Несбалансированно"
            elif (last_item, stack.peek()) not in [("[", "]"), ("{", "}"), ("(", ")")]:
                result = f"Несбалансированно"
            else:
                stack.pop()
        if not stack.isEmpty():
            result = f"Несбалансированно"
    print(result)
    return result


try_balance("))")


