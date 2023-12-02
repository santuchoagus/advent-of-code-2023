import re
import pandas as pd
from functools import reduce

df = pd.read_csv('input.txt', delimiter='%', header=None)
df['input'] = df[0]
df = df.drop(0, axis=1)

# Creates game column with game identifiers
df['game'] = df['input'].str.extract('(\d+):')
df['game'] = df['game'].astype(int)
df_temp = df.copy()

# Removes game string from input text
df_temp['input'] = df_temp['input'].replace(regex=r'(?i)game.*:.', value='')

# explodes input entries by each unique game, for each round separated by ';'
df_temp['input'] = df_temp['input'].str.split(';')
df_temp = df_temp.explode('input')
df = df_temp

colorsMaxCubes = [('red',12), ('green',13), ('blue',14)]

# Creates columns for each cube color
for color, maxCubes in colorsMaxCubes:
    df[color] = df['input'].str.extract('(\d+) {}'.format(color)).fillna(0).astype(int)
    
# Considers only the max quantity of cubes between all the rounds
df = df.groupby('game').agg({'red':'max', 'green':'max', 'blue':'max'}, axis=1).reset_index()

# Multiply the max columns on each game to get the power of a set of cubes
df['power(set)'] = df['red'] * df['green'] * df['blue']

print(df['power(set)'].sum())