import pandas as pd

# Read to csv
data = pd.read_csv("nato_phonetic_alphabet.csv")
letters = data.letter.to_list()
nato_phonetic = data.code.to_list()

# My solution 
output_list = []
word = input("Please enter the word: ").upper()
for word_letter in word:
    if word_letter in letters:
        index_letter = letters.index(word_letter)
        nato_values = nato_phonetic[index_letter]
        output_list.append(nato_values)

print(output_list)


"""
# Another Option

phonetic_dict = {row.letter: row.code for (index, row) in data.iterrows()}
print(phonetic_dict)
word = input("Enter a word: ").upper()
output_list = [phonetic_dict[letter] for letter in word]
print(output_list)
"""