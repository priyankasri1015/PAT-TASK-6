def find_triplet_with_sum(lst, target_sum):
    n = len(lst)

    for i in range(n - 2):
        for j in range(i + 1, n - 1):
            for k in range(j + 1, n):
                if lst[i] + lst[j] + lst[k] == target_sum:
                    return [lst[i], lst[j], lst[k]]

    return None  # Return None if no such triplet is found

# Example usage:
given_list = [10, 20, 30, 9]
target_sum = 59

result_triplet = find_triplet_with_sum(given_list, target_sum)

if result_triplet:
    print(f"The triplet with sum {target_sum} is: {result_triplet}")
else:
    print(f"No triplet found with sum {target_sum}")