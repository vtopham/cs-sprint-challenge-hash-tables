def get_indices_of_item_weights(weights, length, limit):
    """
    YOUR CODE HERE
    """
    # All we need to do is find any two items 
    #the limit minus the first item weight is equal to the other item weight
    #so for each item, we'll check for its complement and hash it if its not there
    #if we find the complement we'll just print out the tuple

    pair = None
    i = 0
    hashtable = {}

    #WHOOPS THIS DOES NOT USE INDEXES
    # while pair == None and i < length:
    #     weight = weights[i]
    #     inv = limit - weight
    #     if inv not in hashtable:
    #         hashtable[weight] = inv
    #     else:
    #         if inv < weight:
    #             pair = (weight, inv)
    #         else:
    #             pair = (inv, weight)
    #     i += 1


    #THIS ONE WORKS
    #TUPLE (index, inv, invindex)
    while pair == None and i < length:
        weight = weights[i]
        inv = limit - weight
        if inv not in hashtable:
            #store the index of this weight if its inverse is not already there
            hashtable[weight] = i
        else:
            #if the inverse is there, then store the tuple with both indexes
            
            pair = (i, hashtable[inv])
        i += 1
    return pair
