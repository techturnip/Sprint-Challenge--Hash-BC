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

    # print length input
    print(f'Length: {length}')

    # loop through tickets and insert into hash table
    for ticket in tickets:
        # insert with source as key and destination as value
        hash_table_insert(hashtable, ticket.source, ticket.destination)

        print(f'Source: {ticket.source}, Dest: {ticket.destination}')

    # first flight has a 'NONE' key for source so we can safely
    # store that ticket's destination as first in the route array
    route[0] = hash_table_retrieve(hashtable, 'NONE')

    # loop and add the other destinations to the route array
    # starting at 1 since we already have the 0th confirmed
    for i in range(1, length):
        # first index is confirmed, key is the src, so we retrieve
        # the next destination by passing the previous route's destination(value)
        # as the src(key) for the next layover... that sounds right... my brain hurts.
        # Route is just a list of destinations
        route[i] = hash_table_retrieve(hashtable, route[i-1])

    print(route)
