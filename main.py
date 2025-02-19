student_dict = {
    "student": ["Angela", "James", "Lily"], 
    "score": [56, 76, 98]
}

#Looping through dictionaries:
for (key, value) in student_dict.items():
    #Access key and value
    pass

import pandas
student_data_frame = pandas.DataFrame(student_dict)

#Loop through rows of a data frame
for (index, row) in student_data_frame.iterrows():
    #Access index and row
    #Access row.student or row.score
    pass

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

#TODO 1. Create a dictionary in this format:
{"A": "Alfa", "B": "Bravo"}
nato_phonetic_alphabet = pandas.read_csv("nato_phonetic_alphabet.csv")
with open("nato_phonetic_alphabet.csv", mode="r") as file:
    nato_phonetic_alphabet = nato_phonetic_alphabet.to_dict()

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
user_word = input("Type a word: ")
user_word = [letter.upper() for letter in user_word]

nato_phonetic_alphabet_df = pandas.DataFrame(nato_phonetic_alphabet)
print(nato_phonetic_alphabet_df)
phonetic_word_list = [row.code for (index, row) in nato_phonetic_alphabet_df.iterrows() if row.letter in user_word]
print(phonetic_word_list)

