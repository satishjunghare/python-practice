# enumerate() is used to loop through the containers printing the index number along with the value present in that particular index.
for key, value in enumerate(['one', 'two', 'three']):
    print (key, value)


# zip() is used to combine 2 similar containers
questions = ["one", "two", "three", "four"]
answers = ["five", "six", "seven", "eight"]

for key, value in zip(questions, answers):
    print("Questions is {0} and answers is {1}".format(key, value))


# using sorted() to print the list in sorted order
lis = [1, 3, 5, 6, 2, 1, 3]
print("The list in sorted order is : ")
for i in sorted(lis):
    print(i, end=" ")

print("\r")