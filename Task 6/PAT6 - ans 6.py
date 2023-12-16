def find_common_duplicates(list1, list2, list3):
    # Find duplicates in each list
    duplicates_list1 = set(x for x in list1 if list1.count(x) > 1)
    duplicates_list2 = set(x for x in list2 if list2.count(x) > 1)
    duplicates_list3 = set(x for x in list3 if list3.count(x) > 1)

    # Find common duplicates across all three lists
    common_duplicates = duplicates_list1.intersection(duplicates_list2, duplicates_list3)

    return list(common_duplicates)

# Example usage
list1 = [1, 2, 4, 3, 2, 5, 6]
list2 = [4, 5, 6, 7, 8, 4]
list3 = [6, 7, 8, 9, 10, 6]

result = find_common_duplicates(list1, list2, list3)

print(f"The common duplicates in the three lists are: {result}")