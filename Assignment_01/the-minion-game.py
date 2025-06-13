def minion_game(string):
    vowels = 'AEIOU'
    rahul_score = 0
    ajay_score = 0
    for i in range(len(string)):
        if string[i] in vowels:
            rahul_score += len(string) - i
        else:
            ajay_score += len(string) - i
    if rahul_score > ajay_score:
        print("Rahul", rahul_score)
    elif rahul_score < ajay_score: 
        print("Ajay", ajay_score)
    else:
        print("Draw")
string = input()
minion_game(string)