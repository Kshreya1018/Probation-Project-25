import random
animal = random.choice(['cat', 'dog', 'lion', 'donkey'])
print("Word:",animal)

l = len(animal)
a =""
c=6
for i in range(c):
    s = input("enter the letter: ")
    if s in animal:
        for j in range(l):
            if animal[j] == s:
                a=a+s
        print("Correct!")
    else:
        c -= 1
        print("wrong guess! chances left:", c)
    print("Word:",a)

    if  a == animal:
        print("congrats! correct answer is", animal)
        break
else:
    print("correct answer was", animal)