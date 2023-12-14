import math


def process_input(data):
    if isinstance(data, dict):
        sorted_dict_asc = dict(sorted(data.items(), key=lambda item: item[1]))
        sorted_dict_desc = dict(sorted(data.items(), key=lambda item: item[1], reverse=True))
        return sorted_dict_asc, sorted_dict_desc
    elif isinstance(data, list):
        letter_count = sum(1 for elem in data if isinstance(elem, str) and elem.isalpha())
        number_count = sum(1 for elem in data if isinstance(elem, (int, float)))
        def is_prime(n):
            if n < 2:
                return False
            for i in range(2, int(n**0.5) + 1):
                if n % i == 0:
                    return False
            return True
        prime_numbers = [elem for elem in data if isinstance(elem, (int,float)) and is_prime(int(elem))]
        return letter_count, number_count, prime_numbers
    elif isinstance(data, str):
        palindromes = [word for word in data.split() if word.lower() == word.lower()[::-1]]
        return palindromes
    else:
        return "Неподдерживаемый тип данных"
input_data = {'b': 2, 'a': 1,  'c': 3}
result = process_input(input_data)
print(result)
input_data = ['abc', 123, 'xyz', 11, 'aba']
result = process_input(input_data)
print(result)
input_data = 'A man a plan a horse'
result = process_input(input_data)
print(result)