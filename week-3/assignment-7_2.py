'''
Python Data Structures

Assignment: 7.2
    Write a program that prompts for a file name, then opens that file and reads through the file, looking for lines of the form:
        X-DSPAM-Confidence:    0.8475
    Count these lines and extract the floating point values from each of the lines and compute the average of those values and produce an output as shown below. Do not use the sum() function or a variable named sum in your solution.
    You can download the sample data at http://www.py4e.com/code3/mbox-short.txt when you are testing below enter mbox-short.txt as the file name.
'''

fileName = input("Enter file name: ")
content = open(fileName)

totalLines = 0
vals = 0
avgVal = 0

for line in content:
    if line.startswith("X-DSPAM-Confidence:") : 
        totalLines += 1
        vals += float(line[20:])

avgVal = vals / totalLines

print("Average spam confidence:", avgVal)