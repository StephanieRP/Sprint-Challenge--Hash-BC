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

    if limit == None:
        return None
    # Declare count property
    count = 0
    # Put array elements into two hash tables, using for loop,
    for i in range(0, len(weights)):
        hash_table_insert(ht, count, weights[i])
        count += 1

    # If the count is one, return None
    if count == 1 or count == 0:
        return None


def print_answer(answer):
    if answer is not None:
        print(str(answer[0] + " " + answer[1]))
    else:
        print("None")
