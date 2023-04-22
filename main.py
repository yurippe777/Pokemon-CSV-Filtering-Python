import pandas as pd
import easygui
import sys

# Read the CSV file into a pandas DataFrame
df = pd.read_csv("pokemon.csv")

while True:
    # Get a list of all types and display a dialog to select one or more types
    types = sorted(set(filter(None, df["Type1"].fillna('').tolist() + df["Type2"].fillna('').tolist())))
    choices = easygui.multchoicebox("Select one or more types to filter by:", "Filter by Type", ['Any'] + types)
    if choices is None:  # Handle close window button click
        sys.exit()
    elif 'Any' not in choices:  # Handle filtering by type
        # Filter the DataFrame by the selected types
        mask_type = df.apply(lambda row: any(x in row[['Type1', 'Type2']].tolist() for x in choices), axis=1)
        df = df.loc[mask_type]

    # Get a list of all abilities and display a dialog to select one ability
    abilities = sorted(set(filter(None, df[["Ability1", "Ability2", "Ability_Hidden"]].fillna('').values.flatten().tolist())))
    choices = easygui.choicebox("Select an ability to filter by:", "Filter by Ability", ['Any'] + abilities)
    if choices is None:  # Handle close window button click
        sys.exit()
    elif 'Any' in choices:  # Handle filtering by ability
        filtered_df = df
    else:
        # Filter the DataFrame by the selected ability
        mask_ability = df.apply(lambda row: choices in row[['Ability1', 'Ability2', 'Ability_Hidden']].tolist(), axis=1)
        filtered_df = df.loc[mask_ability]

    # Save the filtered results to a new CSV file
    if not filtered_df.empty:
        filtered_df = filtered_df[['Name', 'Type1', 'Type2', 'Ability1', 'Ability2', 'Ability_Hidden', 'HP', 'Attack', 'Defense', 'SP_Attack', 'SP_Defense', 'Speed']]
        filtered_df.to_csv("pokemonfiltered.csv", index=False)
        easygui.msgbox("Filtered results saved to pokemonfiltered.csv", "Results")


