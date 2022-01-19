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