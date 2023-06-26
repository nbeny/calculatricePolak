class RPNCalculator:
    def __init__(self):
        self.stack = []

    def calculate(self, expression):
        tokens = expression.split()

        for token in tokens:
            if token.isdigit():
                self.stack.append(int(token))
            elif token in ['+', '-', '*', '/']:
                if len(self.stack) < 2:
                    raise ValueError('Invalid expression')

                b = self.stack.pop()
                a = self.stack.pop()

                if token == '+':
                    self.stack.append(a + b)
                elif token == '-':
                    self.stack.append(a - b)
                elif token == '*':
                    self.stack.append(a * b)
                elif token == '/':
                    if b == 0:
                        raise ValueError('Division by zero')
                    self.stack.append(a / b)
            else:
                raise ValueError('Invalid token')

        if len(self.stack) == 1:
            return self.stack[0]
        else:
            raise ValueError('Invalid expression')

def isPolakInversedFormule(expression):
    stack = []

    try:
        tokens = expression.split()

        for token in tokens:
            if token.isdigit():
                stack.append(int(token))
            elif token in ['+', '-', '*', '/']:
                if len(stack) < 2:
                    return False
                stack.pop()
                stack.pop()
                stack.append(1)
            else:
                return False

        return len(stack) == 1
    except:
        return False
