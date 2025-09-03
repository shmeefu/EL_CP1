# EL 2nd Madlib

# "verb_1a" awake, I almost jumped out of bed. Downstairs, there was a loud sound, similar to the roar of a(n) "animal_1". It was so "adjective_1", I had never heard such a sound in my life! I quietly "verb_1b" down the stairs, 
# trying hard not to make a noise. When I peeked around the corner, I saw a(n) "adjective_2" "animal_1". Right before it could attack me, I suddenly "verb_1b" awake. It was just a dream. How "adjective_1"!

verb1a=input("Name a verb ending in -ing: ")
animal1=input("Name an animal, any animal: ")
adjective1=input("Name an adjective: ")
verb1b=input("Name a verb ending in -ed: ")
adjective2=input("Name a different adjective: ")

sentence1= verb1a + " awake, I almost jumped out of bed."
sentence2= "Downstairs, there was a loud sound, similar to the roar of a(n) " + animal1

story= sentence1 + " " + sentence2

print(story)