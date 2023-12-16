def find_non_repeating_elements(nums):
    # Create a dictionary to store the frequency of each element
    element_frequency = {}

    # Count the frequency of each element in the list
    for num in nums:
        element_frequency[num] = element_frequency.get(num, 0) + 1

    # Find and print the non-repeating elements
    non_repeating_elements = [num for num, freq in element_frequency.items() if freq == 1]
    return non_repeating_elements

# Example usage
user_input = input("Enter a list of integers separated by spaces: ")
nums = list(map(int, user_input.split()))

result = find_non_repeating_elements(nums)

print(f"The non-repeating elements are: {result}")