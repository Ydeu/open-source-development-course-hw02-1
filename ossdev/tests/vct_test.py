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

        self.assertEqual((a * 0.5).get(), [1, 2, 4])

    def test_xor(self):
        a = Vector([2, 2, 1])

        self.assertEqual((a ^ 3).get(), [1, 1, 2])

    def test_length(self):
        a = Vector([0, 2, 4])
        b = Vector([-1, -4, -1])

        self.assertEqual(a.length(), math.sqrt(20))
        self.assertEqual(b.length(), math.sqrt(18))


if __name__ == "__main__":
    unittest.main()  # pragma: no cover
