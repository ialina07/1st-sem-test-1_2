def modulo11_checksum(isbn_number: str):

    digits = [int(char) for char in isbn_number if char.isdigit()]
    if len(digits) != 10:
        return False

    check_digit = digits[-1]

    total = 0
    for i in range(len(digits) - 1):
        weight = 10 - i
        digit = digits[i]
        total += digit * weight

    expected_check_digit = (11 - (total % 11)) % 11
    return check_digit == expected_check_digit
