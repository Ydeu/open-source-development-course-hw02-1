# Simple Vector implementation in python [![Build Status](https://travis-ci.com/Ydeu/open-source-development-course-hw02-1.svg?branch=master)](https://travis-ci.com/Ydeu/open-source-development-course-hw02-1)

Very simple vector implementation supporting basic operations.

## Usage

```python
from ossdev import Vector
a = Vector([0, 1, 2, 3])
print(a)
```

Operations:
- Addition/subtraction with a scalar: a+1 | a-1
- Vector addition/subtraction: a + b| a - b
- Vector multiplication by a scalar value: a * 2
- Vector negation: -a => (1, 2, 3) = (-1, -2, -3)
- Vector reverse: reversed(a) => (1, 2, 3) = (3, 2, 1)
- Vector xor operation by scalar value: (2, 2, 1) ^ 3 = (1, 1, 2)
- Vector length by Euclidean norm.
- Vector comparison by their length.

## Installation

```bash
pip install -U --no-cache . 
```
