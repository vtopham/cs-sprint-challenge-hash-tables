def has_negatives(a):
    """
    YOUR CODE HERE
    """
    # Your code here
    nums = {}
    #find out if the opposite is in there. if it is, then change value to 1 to indicate that there is a pair. otherwise, add the number as a key.
    for x in a:
        if x * -1 not in nums:
            nums[x] = 0
        else:
            nums[x * -1] = 1

    result = []
    for x in list(nums):
        if nums[x] == 1:
            result.append(abs(x))

    return result


if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))
