# -- Example of a client that uses the HTTP.client library
# -- for requesting a JSON object and printing their
# -- contents
import http.client
import json
import termcolor
from P3.seqP3 import Seq

SERVER = 'rest.ensembl.org'

print("\nConnecting to server: {}\n".format(SERVER))

# Connect with the server
conn = http.client.HTTPConnection(SERVER)

# -- Send the request message, using the GET method. We are

conn.request("GET", "/sequence/id/ENSG00000165879?content-type=application/json")

# -- Read the response message from the server
r1 = conn.getresponse()

# -- Print the status line
print("Response received!: {} {}\n".format(r1.status, r1.reason))

# -- Read the response's body
data1 = r1.read().decode("utf-8")

# -- Create a variable with the data,
# -- form the JSON received
information = json.loads(data1)

sequence_text = information['seq']
seqFrat1 = Seq(sequence_text)

# How many bases are there in Frat1 gene?
n_bases = seqFrat1.len()

# How many T bases are there in Frat 1 gene?
count_bases = seqFrat1.count_base()
n_ts = count_bases['Ts']

# Which base is the most popular in the Frat1 gene? percentage?
perc = seqFrat1.perc_bases()
values = list(perc.values())
keys = list(perc.keys())
maximunvalue = max(values)
most_popular_base = keys[values.index(maximunvalue)]

# Printing all data
print('\n')
print('Data from the Frat1 gene:')
print('The number of bases in the Frat1 gene is: {}'.format(n_bases))
print('The total number of T bases is: {}'.format(n_ts))
print('The most popular base in the Frat1 gene is: {}'.format(most_popular_base))
print('The percentage of the most popular base is: {}'.format(maximunvalue))
print('The percentage of As is: {}'.format(perc['As']))
print('The percentage of Ts is: {}'.format(perc['Ts']))
print('The percentage of Cs is: {}'.format(perc['Cs']))
print('The percentage of Gs is: {}'.format(perc['Gs']))