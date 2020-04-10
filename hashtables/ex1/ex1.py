#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)


def get_indices_of_item_weights(weights, length, limit):
    ht = HashTable(16)

    """
    YOUR CODE HERE
    """
    for i in range(length):
            hash_table_insert(ht,weights[i],i)

    for wt in weights:
        if hash_table_retrieve(ht,(limit-wt)) is not None:
            if wt == (limit-wt):
                return (hash_table_retrieve(ht,wt),weights.index(wt))
            zero=max([wt,(limit-wt)])
            one=min([wt,(limit-wt)])
            return (hash_table_retrieve(ht,zero),hash_table_retrieve(ht,one))
            
    return None


def print_answer(answer):
    if answer is not None:
        print(str(answer[0] + " " + answer[1]))
    else:
        print("None")
