import json
import termcolor


f1 = open("person.json", 'r')
f2 = open("person2.json", 'r')
f3 = open("person3.json", 'r')

person1 = json.load(f1)
person2 = json.load(f2)
person3 = json.load(f3)

list_people = [person1, person2, person3]

for person in list_people:
    print()
    termcolor.cprint("Name: ", 'green', end="")
    print(person['Firstname'], person['Lastname'])
    termcolor.cprint("Age: ", 'green', end="")
    print(person['age'])

    phoneNumbers = person['phoneNumber']

    termcolor.cprint("Phone numbers: ", 'green', end='')
    print(len(phoneNumbers))

    for i, num in enumerate(phoneNumbers):
        termcolor.cprint("  Phone {}".format(i))
        termcolor.cprint("  Type: ", 'red', end='')
        print(num['type'])
        termcolor.cprint("  Number:", 'red', end='')
        print(num['number'])
