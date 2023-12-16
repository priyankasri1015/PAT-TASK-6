def has_sublist_with_zero_sum(lst):
    prefix_sum_set = set()
    prefix_sum = 0

    for num in lst:
        prefix_sum += num

        # Check if the current prefix sum has been seen before
        if prefix_sum in prefix_sum_set or prefix_sum == 0:
            return True

        # Add the current prefix sum to the set
        prefix_sum_set.add(prefix_sum)

    return False

# Example usage:
given_list = [4.2, -3, 1, 6]

if has_sublist_with_zero_sum(given_list):
    print("There is a sub-list with a sum equal to zero.")
else:
    print("There is no sub-list with a sum equal to zero.")