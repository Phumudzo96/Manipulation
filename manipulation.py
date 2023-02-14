#Ask the user to enter a sentence
sentence = input("Write down a sentence: ")
str_manip = sentence
print(str_manip)

#create a variable that will count the number of charatacters in the sentence
num_letter = len(str_manip)
print(num_letter)

#create another variable that will find the last letter of the sentence and 
# then in the sentence and replace it with a "@" 
last_word = str_manip[-1]
str_manip = str_manip.replace(last_word , "@")
print(str_manip)

#Take the last three letters and print them out
back_letter = str_manip[-1:-4:-1]
print(back_letter)

#Take the first three letters and the last two letters and and create a word with those five letter
first_last =(str_manip[0:3] + str_manip[-2:])
print(first_last)