# Simple Vector implementation in python [![Build Status](https://travis-ci.com/Ydeu/open-source-development-course-hw02-1.svg?branch=master)](https://travis-ci.com/Ydeu/open-source-development-course-hw02-1)

Very simple vector implementation supporting basic operations.

## Usage

```python
from ossdev import Vector, Matrix
a = Vector([0, 1, 2, 3])
print(a)

m = Matrix.ident(4)
print(m)
print(m + m)
```

Vector Operations:
- Addition/subtraction with a scalar: a+1 | a-1
- Vector addition/subtraction: a + b| a - b
- Multiplication:
  - scalar * vector
  - row-vector * col-vector
  - col-vector * row-vector
- Vector negation: -a => (1, 2, 3) = (-1, -2, -3)
- Vector reverse: reversed(a) => (1, 2, 3) = (3, 2, 1)
- Vector xor operation by scalar value: (2, 2, 1) ^ 3 = (1, 1, 2)
- Vector and operation by scalar/vector
- Vector length by Euclidean norm.
- Vector comparison by their length.

Matrix operations:
- Addition

## Installation

```bash
pip install -U --no-cache . 
```
