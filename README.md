# sens
Sensitivity analysis functions for mathematical models.

## How to use
First import the library and define a function to analyse

```python3
# Import sens
from sens import *

# A function to analyse
def y(x):
    return x[0] / x[1]
```

Calculate the absolute uncertainties (= partial derivatives) around the input (10, 0.1)

```python3
sensitivities(func = y,
              inputs = [10, 0.1],
              relative = False)
```

This yields, as expected:

```python3
array([   10., -1000.])
```

Calculate the relative sensitivities (= elasticities) around the input (10, 0.1)


```python3
sensitivities(func = y,
              inputs = [10, 0.1],
              relative = True)
```

This yields, as expected:

```python3
array([   1., -1.])
```

We can also use a __distribution__ of inputs instead, giving us a distribution of sensitivities. First define the list of distributions. They need to be functions that return a single value upon calling:

```python3
distributions = [lambda: np.random.uniform(7, 8),
                 lambda: np.random.uniform(5, 6)
                ]
```

Now we can calculate the absolute (or the relative) sensitivities for _N_ sampled input vectors:

```python3
result = sensitivities_distributions(func = y,
              input_distribs = distributions,
              N = 100,
              relative = False)
```

This returns a list of _p_ lists with _N_ elements, where _p_ is the number of input parameters (here: 2). The sublists contain the sensitivity coefficients. We can plot them as follows:

```python3
# Plotting libs
import seaborn as sns
import matplotlib.pyplot as plt

# Plot result
sns.kdeplot(result[0])
sns.kdeplot(result[1])

# Aesthetics
sns.despine()
plt.xlabel("Absolute Sensitivity", fontsize=20)
plt.ylabel("Density", fontsize=20)
plt.show()
```

This gives us the following plot:



## Dependencies
- numpy
- numdifftools

## Testing
Just run the _pipeline.sh_ script, which autoformats the code, typechecks it and runs the test suite.
