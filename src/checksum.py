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

def isbn_console_validator():
    """
    Консольная утилита для проверки ISBN-10 номеров.
    Пользователь вводит ISBN, получает результат проверки.
    Выход по вводу -1.
    """
    print("Введите ISBN для проверки или '-1' для выхода")

    while True:
        try:
            user_input = input("\nВведите ISBN: ").strip()

            # Проверка на выход
            if user_input == "-1":
                print("Выход из программы. До свидания!")
                break

            # Проверка на пустой ввод
            if not user_input:
                print("Ошибка: Введена пустая строка")
                continue

            # Удаляем все пробелы для удобства
            isbn_clean = user_input.replace(" ", "")

            # Проверяем ISBN
            if modulo11_checksum(isbn_clean):
                print("correct")
            else:
                print("incorrect")

        except KeyboardInterrupt:
            print("\n\nПрограмма прервана пользователем. До свидания!")
            break
        except Exception as e:
            print(f"Ошибка: {e}. Пожалуйста, попробуйте еще раз.")

if __name__ == "__main__":
    isbn_console_validator()
