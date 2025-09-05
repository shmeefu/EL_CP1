# EL 2nd Idiot Proof

# have the phone number be formated as 123 456 7890

name = input("What is your name?: ").strip().title()
phone = input("What is your phone number?: ")
gpa= int(input("What is your GPA?: "))

#print(gpa.isdigit())







print("Name: {}".format(name))
print("Phone Number: ")
print("GPA: {:.1f}".format(gpa))