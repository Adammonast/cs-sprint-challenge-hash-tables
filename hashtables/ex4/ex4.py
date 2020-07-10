def has_negatives(a):
    """
    YOUR CODE HERE
    """
    # Your code here

    # todo
    # for an input of numbers, find which postive numbers have corresponding negative numbers
    # input: [ 1, -1, 2, 3, -4, -3, 4, -5, 6, 7 ] ---> [ 1, 3, 4 ]
    # unsorted input
    # return value can also be unsorted
    # limit = approximately 5,000,000 elements

    # put negative values in data structure
    # figure out what data structure to use
    # convert list ---> dict (faster lookup)
    # iterate over the input, check if numbers have corresponding inverse values
    # add to dict

    # store numbers that have corresponding negatives
    result = []
    # convert list into dict (use dict comprehension)
    numbers_dict = {num: True for num in a}
    # loop through input a
    for num in a:
        # if the number is NOT negative and if the inverse is already in the dict
        if num > 0 and (num*-1) in numbers_dict:
            # add the number to results
            result.append(num)
    # return result
    return result


if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))
