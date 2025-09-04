# EL 2nd String Methods Notes

# A method is prebuilt code to complete a task thats specific to a data type.
# A stirng is anything surrounded by question marks in code.

name = input("What is your name").strip().title()
# .lower() => makes it all lower case
# .upper() => makes all upper case
# .capitalize => capitalize the first letter
# .title () => capitalizes the first letter of every word

# print("Hello {}, i hate you!".format(name))

# age = input("how old")

# print(age.isdigit())

# print("ermmmmmmmm......" + age + " okay......")

# sentence = "The quick borange fox jumped over the lazy dog! YAY!!!!!!!!!!!"

# word="borange"
# start = (sentence.find(word))
# length = len(word)



#print(sentence[start:start+length]) #to just print the word
# print(sentence.replace(word, "yellow")) #to change the word to another word/something else

age= int(input("how old ar eyou?"))

print("hello {}, its nice to meet you! i cant belive you are {:.2f}!".format(name, age))
print(f"hello {name}, its nice to meet you! i cant belive you are {age:.1f}!")