#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        # hash_table_remove, <- didnt use
                        hash_table_retrieve,
                        # hash_table_resize <- didnt use
                        )


def get_indices_of_item_weights(weights, length, limit):
    ht = HashTable(16)

    """
    YOUR CODE HERE
    """
    result = None
    # 1. loop: insert each item in list into HashTable
    for i in range(length):
        hash_table_insert(ht, weights[i], i)
    # 2. loop: find difference -> difference = limit - value in weight list
    for i in range(length):
        difference = limit - weights[i]
    # 3. if there are other items in HashTable (storage > 0), check if any keys equal the difference
        if len(ht.storage) > 0:
            # 4. so pass difference as key in retrieve function
            if hash_table_retrieve(ht, difference) != None:
                # 5. if retrieve functions returns a value (which is the index), save it
                other_value = hash_table_retrieve(ht, difference)
                # 6. return it in tuple with the iterator i, which is the value we want to return - find max/min values
                result = (max([i, other_value]), min([i, other_value]))

                return result
    # 7. return None if result never found
    return result


def print_answer(answer):
    if answer is not None:
        print(str(answer[0] + " " + answer[1]))
    else:
        print("None")
