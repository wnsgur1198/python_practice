# 행맨게임
import random

guesses=""
turns=2

infile=open('word.txt','r')
lines=infile.readlines()
word=random.choice(lines)

while turns>0:
    failed=0
    for char in word:
        if char in guesses:
            print(char,end="")
        else:
            print("_",end="")
            failed+=1
    if failed==0:
        print("\nyou win")
        break
    print('')
    guess=input("guess the word: ")
    guesses+=guess
    if guess not in word:
        turns-=1
        print('wrong!')
        print(str(turns)+' chance left')
        if turns==0:
            print('answer is '+word)
infile.close()
