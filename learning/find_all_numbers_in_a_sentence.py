#Find all the numbers in a sentence
#sentence = "nancy is 90 years old . She wants 120 tofee and distribute among 75 friends"

# num = []
# for word in sentence.split():
#     if word.isdigit():
#         num.append(word)
        
# print(num)

# if the sentence numbers having floating number
sentence = "nancy is 90.5 years old . She wants 120 tofee and distribute among 75 friends"
num = []
for word in sentence.split():
    if not word.isalpha():
        num.append(word)

print(num)