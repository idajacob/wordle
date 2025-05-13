import random
import csv


def load_word_list():
    with open('wordle_words.csv', newline='') as csvfile:
      reader =csv.reader(csvfile)
      word_list = [row[0] for row in reader if len(row[0]) == 5]
    return word_list

def play_wordle():
    word_list = load_word_list()
    target_word = random.choice(word_list)
    print(f"Target word: {target_word}")

play_wordle()


### TO DO ###

# feedback strategy
# guessing logic
# input code framework
# how to update
# selection