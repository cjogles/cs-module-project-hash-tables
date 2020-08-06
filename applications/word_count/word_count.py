
# " : ; , . - + = / \ | [ ] { } ( ) * ^ &

import re

def word_count(s):
    # Your code here
    # first lowercase everything in string, and ignore characters I don't care about by deleting them
    my_string = s.lower()
    my_string = re.sub("\"", "", my_string)
    my_string = re.sub("\[", "", my_string)
    my_string = re.sub("\]", "", my_string)
    my_string = re.sub("\{", "", my_string)
    my_string = re.sub("\}", "", my_string)
    my_string = re.sub("=", "", my_string)
    my_string = re.sub("\.", "", my_string)
    my_string = re.sub(":", "", my_string)
    my_string = re.sub(";", "", my_string)
    my_string = re.sub(",", "", my_string)
    my_string = re.sub("-", "", my_string)
    my_string = re.sub("\+", "", my_string)
    my_string = re.sub("/", "", my_string)
    my_string = re.sub("\\\\", "", my_string)
    my_string = re.sub("\|", "", my_string)
    my_string = re.sub("\(", "", my_string)
    my_string = re.sub("\)", "", my_string)
    my_string = re.sub("\*", "", my_string)
    my_string = re.sub("\^", "", my_string)
    my_string = re.sub("\&", "", my_string)
    my_string = re.sub("  ", " ", my_string)
    my_string = re.sub("  ", " ", my_string)
    my_string = re.sub("  ", " ", my_string)
    my_string = re.sub("  ", " ", my_string)
    print(my_string)
    # next, split the string into words and put them into a hash table with each key 
    # equaling the given word, and its value initialized to zero
    my_list = my_string.split()
    my_dict = {}
    for i in my_list:
        if i not in my_dict:
            my_dict[i] = 1
        else:
            my_dict[i] += 1

    return my_dict
    
# my example...
# word_count("here^& IS+ a a St-ri/ng ;T\\O *:Pr|ac,t(ICE) on. Why [ don't = \" you try{ } it out? ")

if __name__ == "__main__":
    print(word_count(""))
    print(word_count("Hello"))
    print(word_count('Hello, my cat. And my cat doesn\'t say "hello" back.'))
    print(word_count('This is a test of the emergency broadcast network. This is only a test.'))
