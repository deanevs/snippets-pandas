import pandas as pd
import numpy as np

# create a new dataframe
df = pd.DataFrame({'A': 'foo bar foo bar foo bar foo foo'.split(),
                   'B': 'one one two three two two one three'.split(),
                   'C': np.arange(8), 
                   'D': np.arange(8) * 2})

print(df)

for idx, row in df.iterrows():
    a = row['A']
    if a == 'foo':
        df.at[idx, 'NEW'] = 'ammend'
    else: df.at[idx, 'NEW'] = ''

print(df)

     A      B  C   D
0  foo    one  0   0
1  bar    one  1   2
2  foo    two  2   4
3  bar  three  3   6
4  foo    two  4   8
5  bar    two  5  10
6  foo    one  6  12
7  foo  three  7  14

     A      B  C   D     NEW
0  foo    one  0   0  ammend
1  bar    one  1   2        
2  foo    two  2   4  ammend
3  bar  three  3   6        
4  foo    two  4   8  ammend
5  bar    two  5  10        
6  foo    one  6  12  ammend
7  foo  three  7  14  ammend