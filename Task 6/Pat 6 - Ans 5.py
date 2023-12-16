def distribute_mangoes(mango_bags, num_students):
    # Sort the list of mango bags
    sorted_bags = sorted(mango_bags)

    # Calculate the minimum difference
    min_difference = float('inf')
    min_index = 0

    for i in range(len(sorted_bags) - num_students + 1):
        difference = sorted_bags[i + num_students - 1] - sorted_bags[i]
        if difference < min_difference:
            min_difference = difference
            min_index = i

    # Get the bags for each student
    selected_bags = sorted_bags[min_index:min_index + num_students]

    return selected_bags

# Example usage:
mango_bags = [10, 5, 8, 20, 15]
num_students = 3

selected_bags = distribute_mangoes(mango_bags, num_students)

print("Original Mango Bags:", mango_bags)
print(f"Selected Mango Bags for {num_students} students:", selected_bags)
print("Minimum Difference:", selected_bags[-1] - selected_bags[0])