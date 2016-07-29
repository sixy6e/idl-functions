idl-functions
=============

A collection of IDL functions written in Python.

These functions try to replicate IDL's behaviour as best as possible, while
also keeping in line with Python's PEP8 style guide.

```python
from idl_functions import histogram, randomu

# uniform random numbers between 0 & 256
data = (randomu(seed, [1000]) * 256).astype('uint8')

# histogram
h = histogram(data, omin='omin', omax='omax', reverse_indices='ri', locations='loc')

# access the additional histogram outputs via a dictionary
hist = h['histogram']
omin = h['omin']
omax = h['omax']
ri = h['ri']
loc = h['loc']
```
