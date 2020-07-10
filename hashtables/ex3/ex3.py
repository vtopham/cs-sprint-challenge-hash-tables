def intersection(arrays):
    """
    YOUR CODE HERE
    """
    # Your code here
    #store the numbers that occur in a dictionary with a count. if the count == the number of arrays in the list then it intersects.
    nums = {}
    for arr in arrays:
        for x in arr:
            if x not in nums:
                nums[x] = 1
            else:
                nums[x] += 1
    
    result = []
    for num in list(nums):
        if nums[num] == len(arrays):
            result.append(int(num))

    
    return result


if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
    arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
    arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

    print(intersection(arrays))
