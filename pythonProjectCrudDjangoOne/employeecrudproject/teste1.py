#Given two sentences, return an array that has the words that appear in one sentence and not
#the other and an array with the words in common.

# def uncommon(a, b):
#     list_a = a.split()
#     list_b = b.split()
#     uc = ''
#     for i in list_a:
#         if i not in list_b:
#             uc = uc + " " + i
#     for j in list_b:
#         if j not in list_a:
#             uc = uc + " " + j
#
#     return uc


sentence1 = 'We are really pleased to meet you in our company'
sentence2 = 'Our company will pleased to you for your time'
# print(uncommon(sentence1, sentence2))

list_a = sentence1.split()
list_b = sentence2.split()

sen = ''

for i in list_a:
    if i not in list_b:
        sen = sen+" " + i
for j in list_b:
    if j not in list_a:
        sen = sen+" " + j

print(sen)



