import random
print("Welcome to Hangman!")
words=["apple","banana","python","kiwi","berry"]
x=random.choice(words)
print(x)
c=6
display=[]
for i in range(len(x)):
    display+="_"
print("word:",display)
out=False
while out is False:
    g=input("guess a letter ")
    for j in range(len(x)):
        if(x[j]==g):
            found=True
            display[j]=g
    if(found==True):
        print(f"you did it{display}")
    else:
        print("it's wrong try another one")
        c-=1
        print(f"no.of lives{c}")
    if c==0:
        out=True
    if "_" not in display:
        out=True
        print("you won")



