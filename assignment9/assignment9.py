#Write a program that will rank all pokemon based on their strength level, and save it as a list to a CSV file.



def open_pokemon_dictionary():
    """
    This is a fruitful function that opens the pokemon_data.csv file and reads the contents of the file.
    Then it creates a dictionary with the pokemon names as the keys and the total strength as the values.
    Name is the key and total is the value.
    Returns the dictionary.
    """
    with open('pokemon_data.csv', 'r') as file: #opens the file
        contents = file.read() #reads the contents of the file
        lines = contents.splitlines() #splits the contents by lines
        columns = [line.split(',') for line in lines] #splits the lines by commas and saves them to a list of columns for my sanity
    #sets the header to the first column of the columns list to index the columns
    header = columns[0]
    #gets the index of the name and total columns
    pokemon_name_index = header.index('name')
    pokemon_total_index = header.index('total')
    #excludes the header
    pokemon_data = columns[1:]
    #creates an empty dictionary to store the pokemon name and total strength
    pokemon_dictionary = {}

    #loops through the pokemon data and gets the name and total strength and adds them to the dictionary
    for i in range(len(pokemon_data)):
        pokemon_name = pokemon_data[i][pokemon_name_index]
        pokemon_total = pokemon_data[i][pokemon_total_index]
        pokemon_total = int(pokemon_total)
        pokemon_dictionary[pokemon_name] = pokemon_total
    #returns the dictionary
    return pokemon_dictionary

def pokemon_ranking():
        """
        This is a fruitful function that ranks all pokemon based on their strength level and saves it as a list to a CSV file.
        Returns a success message.
        """

        #opens the pokemon dictionary function
        pokemon_dict = open_pokemon_dictionary()
        #sorts the dictionary by the total values in descending order
        sorted_strength = sorted(pokemon_dict.items(), key = lambda x: x[1], reverse = True)
        
    #creates a CSV file with the  sorted name and total strength of the pokemon
        with open('pokemon_ranking.csv', 'w') as file:
            file.write('name,total\n')
            for pokemon in sorted_strength: #loops through the sorted strength list and writes the name and total strength to the file
                file.write(pokemon[0] + ',' + str(pokemon[1]) + '\n')
        #prints a message if the file was successfully created
        return print('Successfully created the file "pokemon_ranking.csv".')

pokemon_ranking()     