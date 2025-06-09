n = int(input())
words = {}
order = []
for _ in range(n):
    word = input()
    if word not in words:
        order.append(word)
    words[word] = words.get(word, 0) + 1
print(len(words))
print(' '.join(str(words[word]) for word in order))