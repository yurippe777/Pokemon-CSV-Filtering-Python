import pandas as pd
import easygui
import sys
# Read the CSV file into a pandas DataFrame
df = pd.read_csv("pokemon.csv")

while True:
    # Search for pokemon of a certain type
    type1 = easygui.enterbox("Enter a type to search for:")
    if type1 is None:  # Handle close window button click
        sys.exit()
    type1_pokemon = df.loc[(df["Type1"] == type1) | (df["Type2"] == type1)]
    easygui.textbox("Results:", str(type1_pokemon))

    # Search for pokemon of a certain dual type
    type1 = easygui.enterbox("Enter the first type to search for:")
    if type1 is None:  # Handle close window button click
        sys.exit()
    type2 = easygui.enterbox("Enter the second type to search for:")
    if type2 is None:  # Handle close window button click
        sys.exit()
        continue
    dual_type_pokemon = df.loc[(df["Type1"] == type1) & (df["Type2"] == type2)]
    easygui.textbox("Results:", str(dual_type_pokemon))

    # Search for pokemon with a certain ability
    ability = easygui.enterbox("Enter an ability to search for:")
    if ability is None:  # Handle close window button click
        sys.exit()
        break
    ability_pokemon = df.loc[(df["Ability1"] == ability) | (df["Ability2"] == ability) | (df["Ability_Hidden"] == ability)]
    easygui.textbox("Results:", str(ability_pokemon))
