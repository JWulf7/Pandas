# Loading Data into Pandas
import pandas as pd
import re

# Create dataframe from csv data
## to run file in interactive jupyter
poke_df = pd.read_csv('pokemon_data.csv')
## to run file as python script file
# poke_df = pd.read_csv('Pandas\pokemon_data.csv')

# additional data file types
df_xlsx = pd.read_excel('pokemon_data.xlsx')
df_txt = pd.read_csv('pokemon_data.txt', delimiter='\t')

##### PEEK DATA
print(poke_df.head(3))
print(poke_df.tail(3))
print(df_xlsx.head(3))
print(df_txt.head(3))

# Read Headers
print(poke_df.columns)
# Read each Column
print(poke_df['Name'])
# print(poke_df.Name) # same as above
## limited
print(poke_df['Name'][0:5])
## multiple columns
print(poke_df[['Name', 'Type 1', 'HP']])
# Read each Row
print(poke_df.iloc[0])
## multiple rows
print(poke_df.iloc[0:3])
# Read a specific Location (Row,Col)
print(poke_df.iloc[0,1])

## peek each
for index, row in poke_df.iterrows():
    print(index, row)
for index, row in poke_df.iterrows():
    print(index, row['Name'])
# peek rows with "Fire"
poke_df.loc[poke_df['Type 1'] == "Fire"]


#####   SORT/DESCRIBING DATA
poke_df.describe()  # gives high-level type stats (count/mean/standardDeviation/min/max/etc.)
poke_df.sort_values('Name')
# reverse order
poke_df.sort_values('Name', ascending=False)
# sort based on multi columns
poke_df.sort_values(['Type 1', 'HP'])
# sort multi columns - first column ascending, 2nd column descending
poke_df.sort_values(['Type 1', 'HP'], ascending=[1,0])


#####   MAKE CHANGES to DATA
# adding stat columns total to make new total column
## very readable way of summing totals
poke_df['Total_Stat'] = poke_df['HP'] + poke_df['Attack'] + poke_df['Defense'] + poke_df['Sp. Atk'] + poke_df['Sp. Def'] + poke_df['Speed']
poke_df.head(5)
# drop that new column
poke_df = poke_df.drop(columns=['Total_Stat'])
# Add Total_Stat column, using loc and sum() function
poke_df['Total_Stat'] = poke_df.loc[:, 'HP':'Speed'].sum(axis=1)    ## add horizontally (for each row)

# Bump new column to start of stats
## save column names as a list
cols = list(poke_df.columns.values)
# reset/save dataframe ref var to df at columns index 0-4, new col, 5- last old col
poke_df = poke_df[cols[0:4] + [cols[-1]] + cols[4:12]]

poke_df.head(5)

#####   SAVING DATA / EXPORTING INTO DESIRED FORMAT
# poke_df.to_csv('modified.csv')
poke_df.to_csv('modified.csv', index=False) #eliminate the index column 
# poke_df.to_excel('modified.xlsx', index=False)
poke_df.to_csv('modified.txt', index=False, sep='\t')

#####   FILTERING DATA
# filter on multiple columns and
poke_df.loc[(poke_df['Type 1'] == 'Grass') & (poke_df['Type 2'] == 'Poison')]
# filter on multiple columns or
poke_df.loc[(poke_df['Type 1'] == 'Grass') | (poke_df['Type 2'] == 'Poison')]
# filter on multiple columns and numerical conditions
new_df = poke_df.loc[(poke_df['Type 1'] == 'Grass') & (poke_df['Type 2'] == 'Poison') & (poke_df['HP'] > 70)]
## can make checkpoint here if want
# new_df.to_csv('filtered.csv', index=False)
## reset indexes of carried over filtered data indexes, and drop the default added old indexes column, also modify existing df
new_df.reset_index(drop=True, inplace=True)

# filter only contains string
poke_df.loc[poke_df['Name'].str.contains('Mega')]
# filter OUT contains string
poke_df.loc[~poke_df['Name'].str.contains('Mega')]

# filter w/ regex
poke_df.loc[poke_df['Type 1'].str.contains('Fire|Grass', regex=True)]
poke_df.loc[poke_df['Type 1'].str.contains('fire|grass', flags=re.I, regex=True)]   # ignore case of strings

# Get all poke names start w/ 'pi'
poke_df.loc[poke_df['Name'].str.startswith('Pi')]
## same w/ regex
poke_df.loc[poke_df['Name'].str.contains('^pi[a-z]*', flags=re.I, regex=True)]

#####   CONDITIONAL CHANGES








