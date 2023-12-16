def is_happy_number(num):
    seen = set()
    while num != 1 and num not in seen:
        seen.add(num)
        num = sum(int(digit) ** 2 for digit in str(num))
    return num == 1

def count_happy_numbers(numbers):
    happy_count = 0
    for number in numbers:
        if is_happy_number(number):
            happy_count += 1
    return happy_count

# Given Python List
original_list = [10, 501, 22, 37, 100, 999, 87, 351]

# Count happy numbers
happy_count = count_happy_numbers(original_list)

print("Original List:", original_list)
print("Count of Happy Numbers:", happy_count)