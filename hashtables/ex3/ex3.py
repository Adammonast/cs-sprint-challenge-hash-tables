def intersection(arrays):
    """
    YOUR CODE HERE
    """
    # Your code here

    # breakdown:
    # find the intersection of between multiple lists of ints
    # do NOT use: numpy or sets
    # use dict or hashtables
    # given a list of lists that contain integers -->
    """
    [
        [1, 2, 3, 4, 5],
        [12, 7, 2, 9, 1],
        [99, 2, 7, 1,]
    ]
    """
    # compute the _intersection_ --> numbers that exist in ALL lists
    # output should be --> [1, 2] (numbers that exist in all the lists)

    # todo:
    # sort the array of arrays (2d array?) from shortest to longest
    # iterate over the arrays and create a list of dictionaries from them
    # iterate over the values in the SHORTEST array
    # during iteration, check each dict to see if it contains the value
    # if each one contains the value, add it to the result list

    # store everything here
    result = []

    # sort the arrays by shortest to longest
    # call the sorted() function --> returns values in ascending order
    arrays = sorted(arrays, key=len)
    # convert each array to dicts and store them in a new list
    dictionaries = []
    # loop through the arrays of arrays
    for arr in arrays:
        # convert each of them into dict (dictionary comprehension)
        arr_dictionary = {i: True for i in arr}
        # add that dict to the dictionaries list
        dictionaries.append(arr_dictionary)
    # loop through the values of the first SHORTEST array
    for i in arrays[0]:
        # starts as true
        values_in_all = True
        # loop (again) through the dictionaries
        for d in dictionaries:
            # d is a dictionary representing one of the lists
            if i not in d:
                values_in_all = False
        if values_in_all:
            result.append(i)

    return result


if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
    arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
    arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

    print(intersection(arrays))
