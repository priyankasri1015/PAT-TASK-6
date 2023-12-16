def find_minimum_element(sorted_list):
    if not sorted_list:
        return None  # Return None for an empty list
    return sorted_list[0]

# Example usage:
sorted_list = [2, 5, 8, 12, 15, 18, 22]

minimum_element = find_minimum_element(sorted_list)

if minimum_element is not None:
    print(f"The minimum element in the sorted list is: {minimum_element}")
else:
    print("The list is empty.")