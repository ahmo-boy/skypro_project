import unittest
from main_function import check_if_executed, dicts_corrected, mask_card_number

class TestCheckIfExecuted(unittest.TestCase):
    def test_check_if_executed(self):
        data = [{'state': 'EXECUTED'}, {'state': 'PENDING'}, {'state': 'EXECUTED'}, {'state': 'EXECUTED'}, {'state': 'EXECUTED'}]
        result = check_if_executed(data)
        self.assertEqual(len(result), 4)
        for item in result:
            self.assertEqual(item['state'], 'EXECUTED')

class TestDictsCorrected(unittest.TestCase):
    def test_dicts_corrected(self):
        checked_data = [{'date': '2022-04-20T10:30:00.000', 'state': 'EXECUTED', 'id': 1}, {'date': '2022-04-21T10:30:00.000', 'state': 'EXECUTED', 'id': 2}]
        result = dicts_corrected(checked_data)
        self.assertEqual(len(result), 2)
        for item in result:
            self.assertNotIn('state', item)
            self.assertNotIn('id', item)

class TestMaskCardNumber(unittest.TestCase):
    def test_mask_card_number(self):
        card_number = "1234567890123456"
        result = mask_card_number(card_number)
        self.assertEqual(len(result), 4)  # Ожидаем 4 блока
        for block in result:
            self.assertEqual(len(block), 4)  # Ожидаем 4 цифры в каждом блоке

if __name__ == '__main__':
    unittest.main()
