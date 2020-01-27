# Useful doc on Python magic methods:
# https://rszalski.github.io/magicmethods/

import itertools
import math



class Vector:
    def __init__(self, arr=None, size=None):
        self.d = list(arr) if arr is not None else (([0] * size) if size else [])
        self.row = False

    @classmethod
    def from_arr(cls, arr):
        return Vector(arr=list(arr))

    @classmethod
    def from_size(cls, size):
        return Vector(size=size)

    def set(self, arr):
        self.d = arr
        return self

    def get(self):
        return self.d

    def clone(self):
        return Vector.from_arr(list(self.get()))

    @property
    def is_row(self):
        return self.row

    def __len__(self):
        return len(self.d)

    def __repr__(self):
        return str(self.d)

    def __str__(self):
        return 'Vct%s' % self.d

    def __getitem__(self, item):
        return self.d[item]

    def __hash__(self):
        return sum(self.d)

    def __setitem__(self, key, value):
        self.d[key] = value
        return None

    def __cmp__(self, other):
        this_vector = self.length()
        other_vector = other.length()
        return 0 if this_vector == other_vector else (1 if this_vector > other_vector else -1)

    def __neg__(self):
        return Vector([-x for x in self.d])

    def __reversed__(self):
        return Vector(self.d[::-1])

    def __add__(self, other):
        if isinstance(other, int):
            return Vector([x + other for x in self.d])
        elif isinstance(other, Vector):
            if len(self) != len(other): raise ValueError('Incompatible size')
            return Vector([self.d[i] + other[i] for i in range(len(self))])

    # If number of dimensions are different, return the vector to be subtracted from.
    def __sub__(self, other):
        # TODO: implement vector subtraction, comment change to make conflict
        if type(other) is int:
            return Vector([x - other for x in self.d])

        if len(self.d) != len(other.d):
            print("Vectors of different size cannot be subtracted.")
            return self

        return Vector([a + b for a, b in zip(self.d, (-other).d)])
        # you may use __add__() and negation, like return (-self + other)

    def __mul__(self, other):
        if isinstance(other, int):
            return None  # TODO: FIX
        elif isinstance(other, Vector):
            # TODO: add size checks
            if self.is_row == other.is_row:
                return Vector([self.d[i] * other[i] for i in range(len(self))])  # Hadamard product
            elif self.is_row:
                return self.dot(other)  # row x col is a dot-product (check matrix mult.)
            else:
                m = Matrix.square(len(self))  # a matrix
                for i, j in m.index_iter():
                    m[i][j] = self[i] * other[j]
                return m
        else:
            raise ValueError('Invalid operand')

    def __xor__(self, other):
        # TODO: support both vector element-wise XOR and by-scalar xor (like in __add__)
        # TODO: add size check
        if type(other) is int:
            return Vector([x ^ other for x in self.d])

    def __and__(self, other):
        if isinstance(other, int):
            return Vector([x & other for x in self.d])
        elif isinstance(other, Vector):
            # TODO: add size check
            return Vector([self.d[i] & other[i] for i in range(len(self))])
        else:
            raise ValueError('Invalid operand')

    def length(self):
        if len(self) == 0:
            raise ValueError('Undefined for zero-length vector')  # make return 0 instead of an exception
        return math.sqrt(sum(x * x for x in self.d))
        # TODO: implement vector length comp. (hint: return math.sqrt(sum(x*x for x in self.d)))


    def dot(self, other):
        # TODO: implement dot-product, i.e., a.b = \sum_i a[i]*b[i],
        # return sum(self[i]*other[i] for i in range(len(self)))
        return 0

    def transpose(self):
        v = Vector(self.d)
        v.row = not self.row
        return v


class Matrix:
    def __init__(self, dim):
        self._dim = dim
        self.vs = [Vector.from_size(dim[1]) for _ in range(dim[0])]

    @property
    def dim(self):
        return self._dim

    @property
    def rows(self):
        return self.dim[0]

    @property
    def cols(self):
        return self.dim[1]

    def index_iter(self):
        return itertools.product(range(self.rows), range(self.cols))

    def __getitem__(self, item):
        return self.vs[item]

    def __setitem__(self, key, value):
        self.vs[key] = Vector.from_arr(value.get())

    def __repr__(self):
        return ', '.join([repr(x) for x in self.vs])

    def __str__(self):
        return 'Matrix: [\n ' + '\n '.join([repr(x) for x in self.vs]) + '\n]'

    @classmethod
    def from_matrix(cls, o):
        m = Matrix(o.dim)
        for i, j in m.index_iter():
            m[i][j] = o[i][j]
        return m

    @classmethod
    def square(cls, n):
        return cls((n, n))

    @classmethod
    def ident(cls, n):
        m = cls.square(n)
        for i in range(n):
            m[i][i] = 1
        return m

    def check_matrix(self, other):
        if not isinstance(other, Matrix):
            raise ValueError('Not a matrix')

    def check_dim(self, other):
        self.check_matrix(other)
        if self._dim != other.dim:
            raise ValueError('Incompatible matrix')

    def __add__(self, other):
        self.check_dim(other)
        m = Matrix.from_matrix(self)
        for i, j in self.index_iter():
            m[i][j] = m[i][j] + other[i][j]
        return m
