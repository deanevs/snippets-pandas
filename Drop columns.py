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