# Written by Hayden Taylor, 3/21/2019


# Imports 
import requests
import json
import sys
import time

# Variables
endpoint = "http://madlibz.herokuapp.com/api/random?minlength=15&maxlength=15"
response = []

# functions
def animate():
  for i in range(5):
    sys.stdout.write('\rloading |')
    time.sleep(0.1)
    sys.stdout.write('\rloading /')
    time.sleep(0.1)
    sys.stdout.write('\rloading -')
    time.sleep(0.1)
    sys.stdout.write('\rloading \\')
    time.sleep(0.1)
  sys.stdout.write("\rDone! Here's your completed madlib: \n\n")



# Loading API data
r = json.loads(requests.get(endpoint).text)
title = r['title']
blanks = []
val = []

# Loading blank & value response from API into blanks and val arrays
for x in r['blanks']:
  blanks.append(x)
for x in r['value']:
  val.append(x)



print('Welcome to MadLibs! We will ask you a series of questions to complete this madlib: "{}" \n'.format(title))

#Gathering user responses
for i in range(len(blanks)):
 resp = response.append(input("Please input a {}: ".format(blanks[i])))


newlib = []


# Appending response answers to newlib array
for x,y in zip(val, response):
  newlib.append(x + y)

# Displays final madlib

animate()



print(' '.join(newlib)) 
