#! /bin/python3/

name="Syam"

print(name[0]) # first letter
print(name[-1]) # last letter

sentence="This is a sentence"

print(sentence[:4])
print(sentence.split()) #delimiter- default is a space

sentence_split=sentence.split()
sentence_join=" ".join(sentence_split)
print(sentence_join)

quote= " He said, \"I am fine\"" #Escaping double quotes
print(quote)

print("A" in "Apple") #True
print("a" in "Apple") #False

print("a".upper() in "Apple".upper()) #True


movie="Drishyam"

print("My favourite movie is "+movie)
print("My favourite movie is {}".format(movie))
print("My favourite movie is %s" %movie)
print(f"My favourite movie is {movie}")
