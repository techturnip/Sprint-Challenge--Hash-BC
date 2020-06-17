#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)


def get_indices_of_item_weights(weights, length, limit):
    ht = HashTable(16)

    print("\nRUN")

    # print the inputs we are working with
    # print(f'\nLength: {length}')
    # print(f'Weights: {weights}')
    print(f'Limit: {limit}')

    # loop through weights array
    for i in range(0, length):
        # store the weight = weights[i]
        weight = weights[i]
        print(f'Weight: {weight}')

        # store the difference between the weight and limit
        difference = limit - weight
        print(f'Difference: {difference}')

        # check if hash table contains an entry for limit - weight
        retrieved = hash_table_retrieve(ht, difference)
        print(retrieved)

        if retrieved is not None:
            print((i, retrieved))
            return (i, retrieved)

        # store weight's list index as value
        hash_table_insert(ht, weight, i)


def print_answer(answer):
    if answer is not None:
        print(str(answer[0] + " " + answer[1]))
    else:
        print("None")
