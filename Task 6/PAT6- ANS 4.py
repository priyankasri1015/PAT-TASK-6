def sum_of_first_and_last_digit(number):
    # Convert the number to a string to extract digits
    number_str = str(number)

    # Extract the first and last digits
    first_digit = int(number_str[0])
    last_digit = int(number_str[-1])

    # Calculate the sum of the first and last digits
    sum_result = first_digit + last_digit

    return sum_result

# Example usage
user_input = int(input("Enter an integer: "))
result = sum_of_first_and_last_digit(user_input)

print(f"The sum of the first and last digits is: {result}")