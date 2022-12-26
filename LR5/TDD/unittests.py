import unittest
from lab_5.field import field

goods = [
        {'title': 'Ковер', 'price': 2000, 'color': 'green'},
        {'title': 'Диван для отдыха', 'price': 5300, 'color': 'black'}
    ]

class TestEquation(unittest.TestCase):


    def test_calculate(self):
        self.assertEqual(tuple(i for i in field(goods, 'title')), ('Ковер', 'Диван для отдыха'))
        self.assertEqual(tuple(i for i in field(goods, 'title', 'price')), ({'title': 'Ковер', 'price': 2000},
                                                                                 {'title': 'Диван для отдыха',
                                                                                  'price': 5300}))

    def test_type(self):
        with self.assertRaises(TypeError) as e:
            tuple(i for i in field('', 'title'))

    def test_runtime(self):
        with self.assertRaises(RuntimeError) as e:
            tuple(i for i in field(goods))

    def test_key(self):
        with (self.assertRaises(KeyError)) as e:
            tuple(i for i in field(goods, 'title1', 'price'))


if __name__ == '__main__':
    unittest.main()
