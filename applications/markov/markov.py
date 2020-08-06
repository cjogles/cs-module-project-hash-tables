import random

# Read in all the words in one go
with open("input.txt") as f:
    words = f.read()
    my_list = words.split(" ")

# TODO: analyze which words can follow other words
# Your code here

dataset = {}
for i in range(len(my_list) - 1):
    # print(my_list[i]) # every word here
    if my_list[i] not in dataset: # if word is not in dataset
        dataset[my_list[i]] = [my_list[i + 1]] # insert word as key, word after as a value
    else:
        dataset[my_list[i]].append(my_list[i + 1])
        
def find_start_word():
    word_not_found = True
    while word_not_found:
        first_word = random.choice(list(dataset))
        if (first_word[0].isupper()) or (first_word[0] == "\"" and first_word[1].isupper()):
            word_not_found = False
            return first_word

def print_random_sentence(start_word, dataset):
    return_string = start_word
    while True:
        last_letter = start_word[len(start_word) - 1]
        if (last_letter == ".") or (last_letter == "?") or (last_letter == "!") or (last_letter == "\""):
            print(return_string)
            return
        else:
            start_word = random.choice(dataset[start_word])
            return_string = return_string + " " + start_word    
    
# TODO: construct 5 random sentences
# Your code here
first_word = find_start_word()
print_random_sentence(first_word, dataset)
print("_________________________________")
first_word = find_start_word()
print_random_sentence(first_word, dataset)
print("_________________________________")
first_word = find_start_word()
print_random_sentence(first_word, dataset)
print("_________________________________")
first_word = find_start_word()
print_random_sentence(first_word, dataset)
print("_________________________________")
first_word = find_start_word()
print_random_sentence(first_word, dataset)
print("_________________________________")

