'''
Python Data Structures

Assignment: 10.2
    Write a program to read through the mbox-short.txt and figure out the distribution by hour of the day for each of the messages. You can pull the hour out from the 'From ' line by finding the time and then splitting the string a second time using a colon.
        From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
    Once you have accumulated the counts for each hour, print out the counts, sorted by hour as shown below.
'''

fileName = raw_input("Enter file: ")
if len(fileName) < 1 : fileName = "mbox-short.txt"
content = open(fileName)
hours = dict()
for line in content:
    if line.startswith('From '):
        hour = line.split()[5].split(':')[0]
        hours[hour] = hours.get(hour, 0) + 1
for key, value in sorted(hours.items()):
    print (key, value)