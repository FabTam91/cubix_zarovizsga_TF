import unittest
from app import app

class TestCalculator(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()
        self.client.testing = True

    def press_button(self, expression, button):
        return self.client.post('/', data={'expression': expression, 'button': button})

    def test_addition(self):
        response = self.press_button("2+3", "=")
        self.assertIn(b'5', response.data)
        
    def test_subtraction(self):
        response = self.press_button("10-3", "=")
        self.assertIn(b'7', response.data)
    
    def test_multiplication(self):
        response = self.press_button("3*1.5", "=")
        self.assertIn(b'4.5', response.data)
        
    def test_division(self):
        response = self.press_button("12/3", "=")
        self.assertIn(b'4', response.data)

    def test_clear_button(self):
        response = self.press_button("123", "C")
        self.assertNotIn(b'123', response.data)

    def test_invalid_expression(self):
        response = self.press_button("5++", "=")
        self.assertIn(b'Hiba', response.data)

    def test_division_by_zero(self):
        response = self.press_button("5/0", "=")
        self.assertIn(b'Hiba', response.data)

if __name__ == '__main__':
    unittest.main()
