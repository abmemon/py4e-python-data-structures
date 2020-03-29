'''
Python Data Structures

Assignment: 9.4
    Write a program to read through the mbox-short.txt and figure out who has sent the greatest number of mail messages. The program looks for 'From ' lines and takes the second word of those lines as the person who sent the mail. The program creates a Python dictionary that maps the sender's mail address to a count of the number of times they appear in the file. After the dictionary is produced, the program reads through the dictionary using a maximum loop to find the most prolific committer.
'''

fileName = input("Enter file:")
if len(fileName) < 1 : fileName = "mbox-short.txt"
content = open(fileName)
emails = dict()

for line in content:
    word = line.split()
    if line.startswith('From '):
        emails[word[1]] = emails.get(word[1], 0) + 1

greatest = 0
email = ''
for e in emails:
    if  emails[e] > greatest:
        greatest = emails[e]
        email = e
print (email, greatest)