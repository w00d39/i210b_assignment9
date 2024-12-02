# Pokémon Strength Ranking

This program ranks all Pokémon based on their strength level and saves the ranked list to a CSV file.

## Description

The program reads Pokémon data from a CSV file (`pokemon_data.csv`), which contains various attributes of each Pokémon, including their total strength. It then creates a dictionary with Pokémon names as keys and their total strength as values. The Pokémon are sorted based on their strength level in descending order, and the sorted list is saved to a new CSV file (`pokemon_strength_ranked.csv`).

## Functions

### `open_pokemon_dictionary()`

This function opens the `pokemon_data.csv` file and reads its contents. It creates a dictionary with Pokémon names as keys and their total strength as values. The function returns this dictionary.

### `pokemon_ranking()`

This function ranks all Pokémon based on their strength level and saves the ranked list to a CSV file. It returns a success message.

## Usage

1. Ensure you have a CSV file named `pokemon_data.csv` in the same directory as `assignment9.py`. The CSV file should have the following columns: `dexnum`, `name`, `generation`, `type1`, `type2`, `species`, `height`, `weight`, `ability1`, `ability2`, `hidden_ability`, `hp`, `attack`, `defense`, `sp_atk`, `sp_def`, `speed`, `total`, `ev_yield`, `catch_rate`, `base_friendship`, `base_exp`, `growth_rate`, `egg_group1`, `egg_group2`, `percent_male`, `percent_female`, `egg_cycles`, `special_group`.

2. Run the `assignment9.py` script:
