# TraceX
Trace variables and the operations on them using graphviz visualizations.

- wrap the variables in Float() and perform operations
- call draw() function on variables just like print()

NOTE: PRs are currently not accepted for source code. If there are issues/problems, please create an issue.

# Installation
Install using pip
```
pip install tracex
```

# Usage
Integrating TraceX is a piece of cake. All you need is some variables.

## Python API
```python
from tracex import Float, draw

a = Float(2)
b = Float(-3)
c = a * b
d = c + Float(10)
e = Float(-2)
f = d * e

print(f)

draw(f)
```

# Examples
NOTE: PRs are currently accepted for examples. If there are examples you've created, please create a PR.

- TraceX Demo: https://colab.research.google.com/drive/1pmO0X_yWU814_nKCjQSalVddseXSXHLL?usp=sharing
- TraceX Fibonacci: https://colab.research.google.com/drive/168kDOblsbNSReP0m47_1OGuUXVSbxy2S?usp=sharing
