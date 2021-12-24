# Change the Index

# using the index as a unique identifier for slicing
# first check that the column you wish to use is unique
df['Identifier'].is_unique

# now to set this column as the index
 df = df.set_index('Identifier')
 
 # *********************
 
 # convert column from float to int
 >>> df = pd.DataFrame(np.random.rand(3,4), columns=list("ABCD"))
>>> df
          A         B         C         D
0  0.542447  0.949988  0.669239  0.879887
1  0.068542  0.757775  0.891903  0.384542
2  0.021274  0.587504  0.180426  0.574300

>>> df[list("ABCD")] = df[list("ABCD")].astype(int)
>>> df
   A  B  C  D
0  0  0  0  0
1  0  0  0  0
2  0  0  0  0

# ********************************************
 
 # delete column
 
del df['column_name']
# ********************************************

# Drop columns

to_drop = ['Edition Statement',
           'Corporate Author',
           'Corporate Contributors',
           'Former owner',
           'Engraver',
           'Contributors',
           'Issuance type',
           'Shelfmarks']

df.drop(to_drop, inplace=True, axis=1)

# Alternative making it clearer
# df.drop(columns=to_drop, inplace=True)


# ********************************************

# drop dupliactes

df = df.drop_duplicates('COL2')
#same as
#df = df.drop_duplicates('COL2', keep='first')
print (df)
    COL1  COL2
0  a.com    22
1  b.com    45
2  c.com    34
4  f.com    56

# You can also keep only last values:

df = df.drop_duplicates('COL2', keep='last')
print (df)
    COL1  COL2
2  c.com    34
4  f.com    56
5  g.com    22
6  h.com    45

# Or remove all duplicates:

df = df.drop_duplicates('COL2', keep=False)
print (df)
    COL1  COL2
2  c.com    34
4  f.com    56

# *******************************************************
# new answer
# *******************************************************

brand style  rating
0  Yum Yum   cup     4.0
1  Yum Yum   cup     4.0
2  Indomie   cup     3.5
3  Indomie  pack    15.0
4  Indomie  pack     5.0

# By default, it removes duplicate rows based on all columns.

df.drop_duplicates()
    brand style  rating
0  Yum Yum   cup     4.0
2  Indomie   cup     3.5
3  Indomie  pack    15.0
4  Indomie  pack     5.0
To remove duplicates on specific column(s), use subset.

df.drop_duplicates(subset=['brand'])
    brand style  rating
0  Yum Yum   cup     4.0
2  Indomie   cup     3.5
To remove duplicates and keep last occurrences, use keep.

df.drop_duplicates(subset=['brand', 'style'], keep='last')
    brand style  rating
1  Yum Yum   cup     4.0
2  Indomie   cup     3.5
4  Indomie  pack     5.0


# *************************************

# isin

# From ser1 remove items present in ser2.

# Input
ser1 = pd.Series([1, 2, 3, 4, 5])
ser2 = pd.Series([4, 5, 6, 7, 8])

# Solution
ser1[~ser1.isin(ser2)]

# ***********************************


# items common to both series

# Get all items of ser1 and ser2 not common to both.

# Input
ser1 = pd.Series([1, 2, 3, 4, 5])
ser2 = pd.Series([4, 5, 6, 7, 8])

# Solution
ser_u = pd.Series(np.union1d(ser1, ser2))  # union
ser_i = pd.Series(np.intersect1d(ser1, ser2))  # intersect
ser_u[~ser_u.isin(ser_i)]


# **********************************

# iterate over a dataframe

for idx_gm, row_gm in df_gmdn.iterrows():
    gm_gmdn_term = row_gm['TERM_NAME']
    gm_gmdn_code = row_gm['GMDN_CODE']
    
    
# ***************************************

# loc versus iloc

loc indexes on LABEL
iloc indexes on POSITION

Note: Each row has both a label and position


# ***************************************

# Misisng values

# Making a list of missing value types
missing_values = ["n/a", "na", "--"]
df = pd.read_csv("property data.csv", na_values = missing_values)


# select only rows of dataframe with values
df = df[df['col_name'].notnull()]

# can use notna too

# **************************************

# Select Rows

# To select rows whose column value equals a scalar, some_value, use ==:

df.loc[df['column_name'] == some_value]

# To select rows whose column value is in an iterable, some_values, use isin:

df.loc[df['column_name'].isin(some_values)]

# Combine multiple conditions with &:

df.loc[(df['column_name'] >= A) & (df['column_name'] <= B)]

# Note the parentheses. Due to Python's operator precedence rules, & binds more tightly than <= and >=. Thus, the parentheses in the last example are necessary. Without the parentheses

df['column_name'] >= A & df['column_name'] <= B

# is parsed as

df['column_name'] >= (A & df['column_name']) <= B

# which results in a Truth value of a Series is ambiguous error.

# To select rows whose column value does not equal some_value, use !=:

df.loc[df['column_name'] != some_value]

# isin returns a boolean Series, so to select rows whose value is not in some_values, negate the boolean Series using ~:

df.loc[~df['column_name'].isin(some_values)]

# For example,

import pandas as pd
import numpy as np
df = pd.DataFrame({'A': 'foo bar foo bar foo bar foo foo'.split(),
                   'B': 'one one two three two two one three'.split(),
                   'C': np.arange(8), 'D': np.arange(8) * 2})
print(df)
#      A      B  C   D
# 0  foo    one  0   0
# 1  bar    one  1   2
# 2  foo    two  2   4
# 3  bar  three  3   6
# 4  foo    two  4   8
# 5  bar    two  5  10
# 6  foo    one  6  12
# 7  foo  three  7  14

print(df.loc[df['A'] == 'foo'])

     A      B  C   D
0  foo    one  0   0
2  foo    two  2   4
4  foo    two  4   8
6  foo    one  6  12
7  foo  three  7  14

# If you have multiple values you want to include, put them in a list (or more generally, any iterable) and use isin:

print(df.loc[df['B'].isin(['one','three'])])

     A      B  C   D
0  foo    one  0   0
1  bar    one  1   2
3  bar  three  3   6
6  foo    one  6  12
7  foo  three  7  14

# Note, however, that if you wish to do this many times, it is more efficient to make an index first, and then use df.loc:

df = df.set_index(['B'])
print(df.loc['one'])

       A  C   D
B              
one  foo  0   0
one  bar  1   2
one  foo  6  12

# or, to include multiple values from the index use df.index.isin:

df.loc[df.index.isin(['one','two'])]

       A  C   D
B              
one  foo  0   0
one  bar  1   2
two  foo  2   4
two  foo  4   8
two  bar  5  10
one  foo  6  12

# ****************************************************

# String Mehtods

len()	
lower()	
translate()	
islower()
ljust()	
upper()	
startswith()	
isupper()
rjust()	
find()	
endswith()
isnumeric()
center()
rfind()	
isalnum()	
isdecimal()
zfill()	
index()	
isalpha()	
split()
strip()	
index()	
isdigit()	
rsplit()
rstrip()	
capitalize()	
isspace()	
partition()
lstrip()	
swapcase()	
istitle()	
rpartition()