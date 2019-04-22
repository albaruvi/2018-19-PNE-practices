# -- Example of a client that uses the HTTP.client library
# -- for requesting a JSON object and printing their
# -- contents
import http.client
import json
import termcolor

PORT = 8001
SERVER = 'localhost'

print("\nConnecting to server: {}:{}\n".format(SERVER, PORT))

# Connect with the server
conn = http.client.HTTPConnection(SERVER, PORT)

# -- Send the request message, using the GET method. We are
# -- requesting the main page (/)
conn.request("GET", "/listusers")

# -- Read the response message from the server
r1 = conn.getresponse()

# -- Print the status line
print("Response received!: {} {}\n".format(r1.status, r1.reason))

# -- Read the response's body
data1 = r1.read().decode("utf-8")

# -- Create a variable with the data,
# -- form the JSON received
person = json.loads(data1)

for n in [1, 2, 3]:
    print("CONTENT: ")
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
