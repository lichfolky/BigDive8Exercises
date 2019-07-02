import pandas as pd
# import inspect
# import os
# import sys

# import os
# print(os.getcwd())
# print(sys.path)
#
# script filename (usually with path):
# print( inspect.getfile(inspect.currentframe()))
# script directory
# os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))

df = pd.read_csv('SciPython/Data/IMDB_social.csv')
len(df.columns)
for i in range(0, len(df.columns)):
    if (i % 4 == 0):
        print()
    print(f'{df.columns[i]}', end=' / ')

# df.head(4)
# df.tail(3)
# df.shape
# df.info()

print(df.shape)
# df.index

# Manipulation
# print(type(df.duration))
# df.duration
# Select a column
col_select = ['duration', 'budget']
df[col_select].head()
df['budget'].head()
df.budget.head()
df[['duration', 'budget']].head()
df.color == 'Color'
df[df.color == 'Color'].head()  # selection
sel = df[df.color.str.len() > 5].head()  # selection

# loc
df.loc[0]  # by index
df.loc[3:5]
df.loc[5, 'director_name']
df.loc[:5, ['director_name', 'color']]  # key value, columns
df.loc[0:2, df.columns.str.len() <= 5]
df.loc[lambda df: df.color != 'Color'].size
df[df.color != 'Color'].size

# loc setting
df.loc[df.color == 'Color', 'color'] = 'color'  # change 'Color' to 'color'
df.loc[:, 'aaa'] = 'color'  # change 'Color' to 'color'
df.head()
df
# iloc
# same loc but with numbers

# Add a column
df['ciao'] = df.color.apply(lambda x: 'ciao' if x == 'color' else 'no')
df.columns

# Remove a columns
df.drop("aaa", axis=1, inplace=True)
df.columns
df = df.drop("ciao", axis=1)
# alternatively, delete columns using the columns parameter of drop
# data = data.drop(columns="area")

# Group by
grouped = df[['color', 'movie_title', 'language']].groupby('color').language.unique()
# no splitting occurs until it’s needed
grouped
grouped = df[['color', 'movie_title', 'language']].groupby('color').nunique()
grouped
grouped = df.groupby('color')
for name, group in grouped:
    print(name)
    print(group)

type(df.language.value_counts())
df.language.value_counts()
df.head()
df.groupby('color').groups
df.groupby('color').get_group(' Black and White').nunique()
gr = df.groupby('color')
gr.head()
gr.aggregate(sum)
gr.head()
# Pivot
df2 = pd.read_csv(sys.path[0]+'/Data/IMDB_social.csv')
df2.columns
# df2.pivot(index='movie_title', columns='duration')
df.pivot_table(values='director_name', index='movie_title', columns='duration',
               aggfunc='max')
# Join
# Append

# sorting
# .sort_values(ascending=False)
# group fn
df.duration.mean()
df.duration.sum()
