df = pd.DataFrame({'team': ['A', 'A', 'A', 'A', 'B', 'B', 'B', 'B'],
                   'pos': ['Gu', 'Fo', 'Fo', 'Fo', 'Gu', 'Gu', 'Fo', 'Fo'],
                   'points': [18, 22, 19, 14, 14, 11, 20, 28]})

#view DataFrame
df
/*
  team pos  points
0    A  Gu      18
1    A  Fo      22
2    A  Fo      19
3    A  Fo      14
4    B  Gu      14
5    B  Gu      11
6    B  Fo      20
7    B  Fo      28
*/

df_count = df.groupby('team')['pos'].apply(lambda x: (x=='Gu').sum()).reset_index(name='count')
df_count

/*
  team  count
0    A      1
1    B      2
*/

#groupby team and count number of 'points' greater than 15
df_count2 = df.groupby('team')['points'].apply(lambda x: (x>15).sum()).reset_index(name='count')
df_count2

/*
  team  count
0    A      3
1    B      2
*/