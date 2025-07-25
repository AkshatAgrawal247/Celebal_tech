from itertools import combinations
n = int(input())
letters = input().split()
k = int(input())
combs = list(combinations(letters, k))
a_count = sum(1 for c in combs if 'a' in c)
print(f"{a_count / len(combs):.4f}")