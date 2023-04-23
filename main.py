import pandas as pd
import easygui
import sys

# Read the CSV file into a pandas DataFrame
df = pd.read_csv("pokemon.csv")

# Replace NaN values in "Type2", "Ability2", and "Ability_Hidden" columns with "None"
df["Type2"] = df["Type2"].fillna("None")
df["Ability2"] = df["Ability2"].fillna("None")
df["Ability_Hidden"] = df["Ability_Hidden"].fillna("None")

while True:
    # Get a list of all types and display a dialog to select one or more types
    types = sorted(set(filter(None, df["Type1"].fillna('').tolist() + df["Type2"].fillna('').tolist())))
    choices = easygui.multchoicebox("Select one or more types to filter by:", "Filter by Type", ['Any'] + types, preselect=None)
    if choices is None:  # Handle close window button click
        sys.exit()
    elif 'Any' in choices and len(choices) > 1 or len(choices) > 2:  # Handle filtering by type
        easygui.msgbox("Please select no more then two types", "Error")
        continue
    # Filter the DataFrame by the selected types
    elif 'Any' not in choices:
        mask_type = df.apply(lambda row: all(x in row[['Type1', 'Type2']].tolist() for x in choices), axis=1)
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
        result = filtered_df.to_string(index=False)  # Convert DataFrame to a string for display
        easygui.codebox(msg="Filtered results saved to pokemonfiltered.csv", title="Results", text=result)
        df = pd.read_csv("pokemon.csv")
        filtered_df = df
