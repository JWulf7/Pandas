# Loading Data into Pandas
import pandas as pd

# Create dataframe from csv data
## to run file in interactive jupyter
poke_df = pd.read_csv('pokemon_data.csv')
## to run file as python script file
# poke_df = pd.read_csv('Pandas\pokemon_data.csv')

# peek data
print(poke_df.head(3))