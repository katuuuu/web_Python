
class Calculator:

    def __init__(self, last = None):
        Calculator.last = last
        self.operation = []

    def sum(self,a,b):
        res = a + b
        Calculator.last = (f'sum({a}, {b}) == {res}')
        self.operation.append(f'sum({a}, {b}) == {res}')
        return res

    def sub(self, a, b):
        res = a - b
        Calculator.last = (f'sub({a}, {b}) == {res}')
        self.operation.append(f'sub({a}, {b}) == {res}')
        return res

    def mul(self, a, b):
        res = a * b
        Calculator.last = (f'mul({a}, {b}) == {res}')
        self.operation.append(f'mul({a}, {b}) == {res}')
        return res

    def div(self, a, b, mod = False):
        if mod == True:
            res = a % b
            Calculator.last = (f'div({a}, {b}) == {res}')
            self.operation.append(f'div({a}, {b}) == {res}')
        else:
            res = a / b
            Calculator.last = (f'div({a}, {b}) == {res}')
            self.operation.append(f'div({a}, {b}) == {res}')
        return res

    def history(self, operation_number):
        if operation_number <= len(self.operation):
            return self.operation[-operation_number]
        else:
            return None

    @classmethod
    def clear(cls):
        Calculator.last = None
