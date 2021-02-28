"""
Слово - apple
"""

word = "apple"
attempt = 5
split_word = list(word)
# print(split_word)
hidden_word = ["-" for i in split_word]
# print(hidden_word)

hidden_word[0] = "a"
right_ans = 0
finish = False
while finish == False:
    print(hidden_word)
    print("Количество попыток", attempt)
    char = input("Напишите букву: ")
    if char in split_word:
        for i, c in enumerate(split_word):
            if c == char:
                hidden_word[i] = char
                right_ans += 1

            if right_ans == len(split_word):
                print("Вы выиграли")
                finish = True
    else:
        attempt -= 1

    if attempt == 0:
        print("Вы проиграли")
        finish = True

print("Игра окончена")
