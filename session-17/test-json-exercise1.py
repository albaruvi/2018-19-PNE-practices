import json
import termcolor


f1 = open("person-exercise1.json", 'r')

person = json.load(f1)

for n in [1, 2, 3]:
    print()
    termcolor.cprint("Name: ", 'green', end="")
    print(person['Firstname'][n-1], person['Lastname'][n-1])
    termcolor.cprint("Age: ", 'green', end="")
    print(person['age'][n-1])

    phoneNumbers = person['phoneNumber'][n-1]

    termcolor.cprint("Phone numbers: ", 'green', end='')
    print(len(phoneNumbers))

    for i, num in enumerate(phoneNumbers):
        termcolor.cprint("  Phone {}".format(i))
        termcolor.cprint("  Type: ", 'red', end='')
        print(num['type'])
        termcolor.cprint("  Number:", 'red', end='')
        print(num['number'])
