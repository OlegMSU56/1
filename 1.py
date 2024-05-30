'richiest', 'orichalcum', 'cheers', 'richies'
def single_root_words(root_world, *other_words):
    same_words = []
    for j in other_words:
        k = j.lower()
        if root_world.count(k):
            j = k.capitalize()
            same_words.append(j)
    for i in other_words:
        if i.count(root_world) or root_world.count(i):
            same_words.append(i)

    return same_words

result1 = single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies')
result2 = single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel')
print(result1)
print(result2)


'''
'rich', 'richiest', 'orichalcum', 'cheers', 'richies'
Напишите функцию single_root_words, которая принимает одно обязательное слово в параметр root_word, 
а далее неограниченную последовательность в параметр *other_words.
Функция должна составить новый список same_words только из тех слов списка other_words, 
которые содержат root_word или наоборот root_word содержит одно из этих слов. 
После вернуть список same_words в качестве результата своей работы.

Пункты задачи:
1. Объявите функцию single_root_words и напишите в ней параметры root_world и *other_words.
2. Создайте внутри функции пустой список same_words, который пополнится нужными словами.
3. При помощи цикла for переберите предполагаемо подходящие слова.
4. Пропишите корректное относительно задачи условие, при котором добавляются слова в результирующий список same_words.
5. После цикла верните образованный функцией список same_words.
6. Вызовите функцию single_root_words и выведете на экран(консоль) возвращённое ей занчение.

Вывод на консоль:
['richiest', 'orichalcum', 'richies']
['Able', 'Disable']

Примечания:
1. При проверке наичлия одного слова в составе другого стоит учесть, что регистр символов не должен влять ни на что. ('Disablement' - 'Able')
2. В сосновном в этой задаче вам понадобяться методы строк: count() и lower()/upper().
'''