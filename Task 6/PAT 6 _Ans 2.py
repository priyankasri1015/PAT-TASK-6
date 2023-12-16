def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

original_list = [10, 501, 22, 37, 100, 999, 87, 351]

prime_numbers = []
prime_count = 0

for number in original_list:
    if is_prime(number):
        prime_numbers.append(number)
        prime_count += 1

print("Original List:", original_list)
print("Prime Numbers List:", prime_numbers)
print("Count of Prime Numbers:", prime_count)