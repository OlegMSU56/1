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
