def count_words_and_longest_word(input_string):
    words = input_string.split()
    word_count = len(words)
    longest_word = max(words, key=len, default="")
    return word_count, longest_word
input_string = "Это строка с примером для задания 2.1."
count, longest = count_words_and_longest_word(input_string)
print(f"Количество слов: {count}")
print(f"Самое длинное слово: {longest}")