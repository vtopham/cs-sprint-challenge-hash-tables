#  Hint:  You may not need all of these.  Remove the unused functions.
class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    """
    YOUR CODE HERE
    """
    # hash the table
    itinerary = {}
    for ticket in tickets:
        itinerary[ticket.source] = ticket.destination
    
    route = []

    cur_loc = "NONE"
    # next_loc = itinerary["NONE"]
    
    #add locations to an array
    for x in range(length):
        #append the next place, which is the value of the current place
        route.append(itinerary[cur_loc])
        #move the marker
        cur_loc = itinerary[cur_loc]
        
        
    print(route)
    return route
