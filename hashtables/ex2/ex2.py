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
    #route =[]
    """
    YOUR CODE HERE
    """
    # populate the hashtable with source and destination
    for ticket in tickets:
        hash_table_insert(hashtable,ticket.source,ticket.destination)
    
    # starter node is source = "NONE"
    node = hash_table_retrieve(hashtable,"NONE")
    
    #iterate thro the next destination
    for i in range(length-1):
        route[i]=node
        #route.append(node)
        node = hash_table_retrieve(hashtable,node)
    
    route = route[:-1]
    #no need if its a new list
    return route