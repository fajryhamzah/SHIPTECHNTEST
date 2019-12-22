import unittest
from middle import get_mid_node, generate_linklist

class MidNodeTest(unittest.TestCase):
    def test_single_list(self):
        data = generate_linklist([1])
        res = get_mid_node(1,data)
        self.assertEqual(res, 1)

    def test_odd_list(self):
        data = generate_linklist([1,2,3,4,5])
        res = get_mid_node(5,data)
        self.assertEqual(res, 3)

    def test_even_list(self):
        data = generate_linklist([1,2,3,4,5,6])
        res = get_mid_node(6,data)
        self.assertEqual(res, 4)

    def test_empty_list(self):
        data = generate_linklist([])
        res = get_mid_node(1,data)
        self.assertEqual(res, None)


if __name__ == '__main__':
    unittest.main()