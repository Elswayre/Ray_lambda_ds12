print('hello world')

import pandas

from my_ray_lambda_ds12.my_mod import enlarge

df = pandas.DataFrame({'state': ['ct', 'co', 'ca', 'tx']})
print(df.head())

x = 5
print('number is', x)
print('enlarged number is', enlarge(x))