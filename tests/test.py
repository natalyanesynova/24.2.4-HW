import pytest
from app.calculator import Calculator

class TestCalc:
    def setup(self):
        self.calc = Calculator

    def test_adding_success(self):
        assert self.calc.adding(self, 1, 3) == 4

    def test_multiply_success(self):
        assert self.calc.multiply(self, 3, 5) == 15

    def test_division_success(self):
        assert self.calc.division(self, 8, 4) == 2

    def test_subtraction_success(self):
        assert self.calc.subtraction(self, 7, 4) == 3

    def teardown(self):
        print('Выполнение метода Teardown')