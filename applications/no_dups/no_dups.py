def no_dups(s):
    # Your code here
    my_hash_table = {}
    my_string = s.split(" ")
    result = []
    for i in my_string:
        if i not in my_hash_table:
            my_hash_table[i] = i
        else:
            continue
    for i in my_hash_table.items():
        result.append(i[0])
    result = (" ").join(result)
    return result



if __name__ == "__main__":
    print(no_dups(""))
    print(no_dups("hello"))
    print(no_dups("hello hello"))
    print(no_dups("cats dogs fish cats dogs"))
    print(no_dups("spam spam spam eggs spam sausage spam spam and spam"))