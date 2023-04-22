import pandas as pd
import easygui
import sys

# Read the CSV file into a pandas DataFrame
df = pd.read_csv("pokemon.csv")

while True:
    # Get a list of all types and display a dialog to select one or more types
    types = sorted(set(df["Type1"].fillna('').tolist() + df["Type2"].fillna('').tolist()))
    choices = easygui.multchoicebox("Select one or more types to filter by:", "Filter by Type", types)
    if choices is None:  # Handle close window button click
        sys.exit()
    elif len(choices) == 0:  # Handle no type selected
        continue

    # Filter the DataFrame by the selected types
    mask = df.apply(lambda row: any(x in row[['Type1', 'Type2']].tolist() for x in choices), axis=1)
    filtered_df = df.loc[mask]

    # Get a list of all abilities and display a dialog to select one or more abilities
    abilities = sorted(set(filtered_df[["Ability1", "Ability2", "Ability_Hidden"]].fillna('').values.flatten().tolist()))
    choices = easygui.multchoicebox("Select one or more abilities to filter by:", "Filter by Ability", abilities)
    if choices is None:  # Handle close window button click
        sys.exit()
    elif len(choices) == 0:  # Handle no ability selected
        continue

    # Filter the DataFrame by the selected abilities
    mask = filtered_df.apply(lambda row: any(x in row[['Ability1', 'Ability2', 'Ability_Hidden']].tolist() for x in choices), axis=1)
    filtered_df = filtered_df.loc[mask]

    # Save the filtered results to a new CSV file
    filtered_df = filtered_df[['Name', 'Type1', 'Type2', 'Ability1', 'Ability2', 'Ability_Hidden', 'HP', 'Attack', 'Defense', 'SP_Attack', 'SP_Defense', 'Speed']]
    filtered_df.to_csv("pokemonfiltered.csv", index=False)

    easygui.msgbox("Filtered results saved to pokemonfiltered.csv", "Results")


