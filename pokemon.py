# Loading Data into Pandas
import pandas as pd

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
