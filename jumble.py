import random

# the list of words, hints, tuples
word_hint = [
('mouse', 'eats cheese'),
('automobile', 'uses gasoline'),
('boat', 'floats on water'),
('Liberty Mutual', 'best auto insurance'),
('Liberty Mutual', 'best home insurance'),
('Donald Trump', 'best president since George Washington, not')
]

# shuffle the word_hint list and pick a random word and its hint
random.shuffle(word_hint)
word = word_hint[0][0]
hint = word_hint[0][1]

# scramble word via list of char
char_list = list(word)
random.shuffle(char_list)
scramble = "".join(char_list)

# show possible result
print("scramble = {}\nhint = {}".format(scramble, hint))