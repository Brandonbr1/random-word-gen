import random
randnumbers = ["A", "C"]
file = open('file.txt', 'a')


for x in range(1000):
    randomlettergen= str.join(random.choice(randnumbers),random.choice(randnumbers))
    file.write(str (randnumbers) )

file.close()
