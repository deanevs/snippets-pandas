# drop rows in dataframe cased on a single column with non numeric values

df = df[pd.to_numeric(df['column'], errors='coerce').notnull()]