#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)


class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    hashtable = HashTable(length)
    route = [None] * length

    """
    YOUR CODE HERE
    """
    # 1. loop: tickets and insert each ticket in HashTable
    for i in range(length):
        hash_table_insert(hashtable, tickets[i].source, tickets[i].destination)
    # 2. retrieve value in HT where key == None, meaning the first ticket of trip
    first_item = hash_table_retrieve(hashtable, "NONE")
    # 3. make that first item in route array
    route[0] = first_item
    # 4. loop: starting at second slot in route array range(1, length)
    for i in range(1, length):
        # 5. pass the item before as the key in ht retrieval to get next item
        next_item = hash_table_retrieve(hashtable, route[i-1])
        # 6. save value, and set as the current (ith) item in route array
        route[i] = next_item
        print("Your Route: ", route)
    # 7. return the route
    return route
