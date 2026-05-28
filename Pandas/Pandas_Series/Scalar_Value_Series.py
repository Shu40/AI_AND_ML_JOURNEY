import pandas as pd

scalar_value = 42
series = pd.Series(scalar_value, index=['a', 'b', 'c', 'd', 'e'])
print(series)


dict_scalar = pd.Series({'a': 42, 'b': 42, 'c': 42, 'd': 42, 'e': 42})
print(dict_scalar)
