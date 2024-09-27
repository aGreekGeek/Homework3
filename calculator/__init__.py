from typing import List, Type

class Calculation:
    def __init__(self, operation: str, operands: List[float]):
        self.operation = operation
        self.operands = operands

    def get_result(self) -> float:
        if self.operation == 'add':
            return sum(self.operands)
        elif self.operation == 'subtract':
            return self.operands[0] - self.operands[1]
        elif self.operation == 'multiply':
            return self.operands[0] * self.operands[1]
        elif self.operation == 'divide':
            if self.operands[1] == 0:
                raise ZeroDivisionError("Cannot divide by zero")
            return self.operands[0] / self.operands[1]

class Calculator:
    history: List[Type[Calculation]] = []

    @staticmethod
    def add(a: float, b: float) -> float:
        result = a + b
        Calculator.history.append(Calculation('add', [a, b]))
        return result

    @staticmethod
    def subtract(a: float, b: float) -> float:
        result = a - b
        Calculator.history.append(Calculation('subtract', [a, b]))
        return result

    @staticmethod
    def multiply(a: float, b: float) -> float:
        result = a * b
        Calculator.history.append(Calculation('multiply', [a, b]))
        return result

    @staticmethod
    def divide(a: float, b: float) -> float:
        if b == 0:
            raise ZeroDivisionError("Cannot divide by zero")
        result = a / b
        Calculator.history.append(Calculation('divide', [a, b]))
        return result

    @classmethod
    def get_last_calculation(cls) -> Calculation:
        return cls.history[-1]

    @classmethod
    def clear_history(cls):
        cls.history.clear()

    @classmethod
    def get_history(cls) -> List[Type[Calculation]]:
        return cls.history
