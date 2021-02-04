import unittest
from ordered_list import *

class TestLab4(unittest.TestCase):

    def test_simple(self):
        t_list = OrderedList()
        t_list.add(10)
        self.assertEqual(t_list.python_list(), [10])
        self.assertEqual(t_list.size(), 1)
        self.assertEqual(t_list.index(10), 0)
        self.assertTrue(t_list.search(10))
        self.assertFalse(t_list.is_empty())
        self.assertEqual(t_list.python_list_reversed(), [10])
        self.assertTrue(t_list.remove(10))
        t_list.add(10)
        self.assertEqual(t_list.pop(0), 10)
    
    # Tests search
    def test_OrderedList_1(self):
        t_list = OrderedList()
        self.assertFalse(t_list.search(5))
        t_list.add(6)
        self.assertFalse(t_list.search(5))
        self.assertTrue(t_list.search(6))
        t_list.add(2)
        t_list.add(15)
        self.assertTrue(t_list.search(6))
        
    # Test index
    def test_OrderedList_2(self):
        t_list = OrderedList()
        self.assertEqual(t_list.index(3), None)
        t_list.add(1)
        t_list.add(3)
        t_list.add(5)
        t_list.add(7)
        self.assertEqual(t_list.index(6), None)
        self.assertEqual(t_list.index(1), 0)
        self.assertEqual(t_list.index(5), 2)
        self.assertEqual(t_list.index(7), 3)
    
    # Tests a variety of cases for add and remove
    def test_OrderedList_3(self):
        t_list = OrderedList()
        self.assertTrue(t_list.is_empty())
        t_list.add(4)
        t_list.add(3)
        t_list.add(5)
        t_list.add(1)
        t_list.add(10)
        t_list.add(6)
        self.assertFalse(t_list.add(6))
        self.assertFalse(t_list.remove(7))
        self.assertTrue(t_list.remove(1))
        self.assertTrue(t_list.remove(10))
        self.assertTrue(t_list.remove(4))
        self.assertEqual(t_list.python_list(), [3, 5, 6])
    
    # Tests index error is raised for invalid indexs when using pop
    def test_OrderedList_4(self):
        t_list = OrderedList()
        with self.assertRaises(IndexError):
            t_list.pop(-1)
        with self.assertRaises(IndexError):
            t_list.pop(0)
        t_list.add(1)
        with self.assertRaises(IndexError):
            t_list.pop(1)
            
    # Tests pop
    def test_OrderedList_5(self):
        t_list = OrderedList()
        t_list.add(4)
        t_list.add(3)
        t_list.add(5)
        t_list.add(1)
        t_list.add(10)
        t_list.add(6)
        self.assertEqual(t_list.pop(0), 1)
        self.assertEqual(t_list.pop(4), 10)
        self.assertEqual(t_list.pop(1), 4)
        self.assertEqual(t_list.python_list_reversed(), [6, 5, 3])
    
    # Tests python list for empty lists
    def test_OrderedList_6(self):
        t_list = OrderedList()
        self.assertEqual(t_list.python_list(), [])
        self.assertEqual(t_list.python_list_reversed(), [])
        


if __name__ == '__main__': 
    unittest.main()
