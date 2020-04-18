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
