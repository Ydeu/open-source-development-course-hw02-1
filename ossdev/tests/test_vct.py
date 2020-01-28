#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: ossdev

import unittest
from ossdev import Vector
import math


class VectorTest(unittest.TestCase):
    """Simple vector tests"""

    def __init__(self, *args, **kwargs):
        super(VectorTest, self).__init__(*args, **kwargs)

    def test_add(self):
        a = Vector([0, 1, 2, 3])
        b = Vector([3, 2, 1, 0])
        c = a + b

        self.assertEqual(c.get(), [3, 3, 3, 3])

    def test_cmp(self):
        b = Vector([0, 1, 2, 3])
        c = Vector([0, 1, 2, 3])
        d = Vector([0, 1, 2, 4])
        e = Vector([1, 2, 3])

        self.assertEqual(b.__cmp__(c), 0)
        self.assertEqual(d.__cmp__(c), 1)
        self.assertEqual(e.__cmp__(d), -1)
        self.assertEqual(d.__cmp__(e), 1)

    def test_neg(self):
        a = Vector([-1, 0, 1])

        self.assertEqual((-a).get(), [1, 0, -1])

    def test_reversed(self):
        a = Vector([1, 2, 3])

        self.assertEqual(reversed(a).get(), [3, 2, 1])

    def test_sub(self):
        a = Vector([-1, -2, -3])
        b = Vector([-1, -2, -3])
        result = a - b

        self.assertEqual(result.get(), [0, 0, 0])

    def test_mul(self):
        a = Vector([2, 4, 8])
        b = Vector([1, 2, 4])
        c = Vector([2, 2, 2])

        self.assertEqual((a * 0.5).get(), [1, 2, 4])
        self.assertEqual((a * b).get(), [2, 8, 32])
        self.assertEqual(c.transpose() * b, 14)

    def test_xor(self):
        a = Vector([2, 2, 1])

        self.assertEqual((a ^ 3).get(), [1, 1, 2])

    def test_length(self):
        a = Vector([0, 2, 4])
        b = Vector([-1, -4, -1])

        self.assertEqual(a.length(), math.sqrt(20))
        self.assertEqual(b.length(), math.sqrt(18))
        self.assertAlmostEqual(Vector([2, 4]).length(), 4.47213595499, 3)
        self.assertAlmostEqual(Vector([2, 4, 5]).length(), 6.708203932499369, 3)
        self.assertEqual(Vector([]).length(), 0)

    def test_dot(self):
        a = Vector([1, 2])
        b = Vector([2, -1])

        self.assertEqual(a.dot(b), 0)

    def test_and(self):
        a = Vector([2, 2, 2])
        b = Vector([1, 1, 1])
        c = 3

        self.assertEqual(a.__and__(b).get(), [0, 0, 0])
        self.assertEqual(a.__and__(c).get(), [2, 2, 2])
        self.assertEqual(b.__and__(a).get(), [0, 0, 0])

    def test_setitem(self):
        a = Vector([2, 3, 5])
        first_element = a[0]

        a.__setitem__(0, 10.752)
        self.assertEqual(a[0], first_element)
        a.__setitem__(0, "meh")
        self.assertEqual(a[0], first_element)


if __name__ == "__main__":
    unittest.main()  # pragma: no cover
