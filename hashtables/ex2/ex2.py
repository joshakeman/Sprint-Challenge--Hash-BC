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

# tickets = [
#   Ticket("PIT", "ORD" ),
#   Ticket("XNA", "CID" ),
#   Ticket("SFO", "BHM" ),
#   Ticket("FLG", "XNA" ),
#   Ticket("NONE", "LAX" ),
#   Ticket("LAX", "SFO" ),
#   Ticket("CID", "SLC" ),
#   Ticket("ORD", "NONE" ),
#   Ticket("SLC", "PIT" ),
#   Ticket("BHM", "FLG" )
# ]


def reconstruct_trip(tickets, length):
    hashtable = HashTable(length)
    route = [None] * length

    """
    YOUR CODE HERE
    """

    for i in tickets:
        # print(f'source is {i.source}, distination is {i.destination}')
        hash_table_insert(hashtable, i.source, i.destination)
    
    start = hash_table_retrieve(hashtable, 'NONE')
    # print(start)

    route = [start]
    current = start

    while len(route) < length:
        next = hash_table_retrieve(hashtable, current)
        route.append(next)
        current = next

    # print(route)
    return route

# reconstruct_trip(tickets, len(tickets))

# ticket_1 = Ticket("NONE", "PDX")
# ticket_2 = Ticket("PDX", "DCA")
# ticket_3 = Ticket("DCA", "NONE")

# tickets = [ticket_1, ticket_2, ticket_3]

# expected = ["PDX", "DCA", "NONE"]
# result = reconstruct_trip(tickets, 3)

# print(result)