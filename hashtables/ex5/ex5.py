# Your code here



def finder(files, queries):
    """
    YOUR CODE HERE
    """
    # seperate all filepaths into component parts separated by "/"
    # store each component part as a key and then the full path in an array of values
    # for each query, check hash table for that value
    hashtable = {}

    for ind in files:
        #get individual arrays of file path pieces
        arr = ind.split("/")
        for item in arr:
            if item not in hashtable:
                hashtable[item] = []
            hashtable[item].append(ind)

    #now we have a hashtable of all possible querie and paths. Now for each query, add all paths to the results array
    result = []
   
    for q in queries:
       if q in hashtable:
           result.extend(hashtable[q])

    return result


if __name__ == "__main__":
    files = [
        '/bin/foo',
        '/bin/bar',
        '/usr/bin/baz'
    ]
    queries = [
        "foo",
        "qux",
        "baz"
    ]
    print(finder(files, queries))

