def get_indices_of_item_weights(weights, length, limit):
    """
    YOUR CODE HERE
    """
    # Your code here

    # breakdown:
    # given a package with a weight limit `limit` and a list `weights` of item weights
    # implement function that finds two items whose SUM of weight EQUALS the weight limit
    # function returns a tuple of integers ---> (zero, one)
    # each element represents the item weights of the two packages
    # The higher valued index should be placed in the `zeroth` index and the smaller index should be placed in the `first` index
    # If such a pair doesn’t exist: function should return `None`.
    # linear time - as input increases, runtime/space used will grow at the SAME rate --> O(n)

    # todo:
    # check if the length is greater/equal to 1 (if it doesn't have more than one number, we return none)
    # check if the weights numbers are the same, return in the proper order
    # convert weights list to dict
    # iterate over the weights
    # check if the limit - the weight is within the dictionary
    # get the current index to compare to the index of limit - curret weight
    # evaluate values and return them sorted appropriately ---> (greater, smaller)

    # check the length first ---> return None
    if length <= 1:
        return None

    # instance were weights has two numbers that are the SAME
    if length == 2:
        if weights[0] == weights[1] and weights[0] + weights[1] == limit:
            return (1, 0)

    # use enumerate for an iterable enumerate object ---> each iteration will create a tuple containing an index and value
    # convert weights to dict (use dict comprehension)
    weights_dict = {n: idx for idx, n in enumerate(weights)}

    # loop through weights
    for w in weights:
        # if the limit minus the current weight is in the dict,
        if (limit - w) in weights_dict:
            # get index of current weight
            current_idx = weights_dict[w]
            # get index of limit minus the current weight
            sub_idx = weights_dict[limit-w]
            # figure out which one is the larger index
            largest = current_idx if current_idx > sub_idx else sub_idx
            smallest = current_idx if current_idx < sub_idx else sub_idx
            return (largest, smallest)

    return None
