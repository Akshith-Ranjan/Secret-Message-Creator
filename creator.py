#!/usr/bin/python

import os
import shutil
import sys

mapping = {
    'a': 0,
    'b': 1,
    'c': 2,
    'd': 3,
    'e': 4,
    'f': 5,
    'g': 6,
    'h': 7,
    'i': 8,
    'j': 9,
    'k': 10,
    'l': 11,
    'm': 12,
    'n': 13,
    'o': 14,
    'p': 15,
    'q': 16,
    'r': 17,
    's': 18,
    't': 19,
    'u': 20,
    'v': 21,
    'w': 22,
    'x': 23,
    'y': 24,
    'z': 25,
    '.': 26,
    ' ': 27
}
a = [
    'athens.jpg',
    'austin.jpg',
    'bangalore.jpg',
    'barcelona.jpg',
    'beijing.jpg',
    'berkeley.jpg',
    'bogota.jpg',
    'bristol.jpg',
    'bucharest.jpg',
    'buenos aires.jpg',
    'cairo.jpg',
    'chennai.jpg',
    'chicago.jpg',
    'colombo.jpg',
    'dallas.jpg',
    'delhi.jpg',
    'edinbrugh.jpg',
    'gainesville.jpg',
    'houston.jpg',
    'hyderabad.jpg',
    'istanbul.jpg',
    'ithaca.jpg',
    'jacksonville.jpg',
    'karachi.jpg',
    'kiev.jpg',
    'london.jpg',
    'los angeles.jpg',
    'madrid.jpg',
    'manchester.jpg',
    'miami.jpg',
    'new york.jpg',
    'oakland.jpg',
    'pune.jpg',
    'rochester.jpg',
    'san diego.jpg',
    'san jose.jpg',
    'sao paulo.jpg',
    'seattle.jpg',
    'seoul.jpg',
    'shanghai.jpg',
    'singapore.jpg',
    'sunnyvale.jpg',
    'sydney.jpg',
    'tel aviv.jpg',
    'zimbabwe.jpg'
]


if os.path.isdir(r"./alphabet"):
    alpha_files = os.listdir(r"./alphabet/")
    if len(alpha_files) != 28:
        print "All alphabet images dosent exist( 26 letters, '.' and ' ' )"
        print "exiting..."
        sys.exit()
else:
    print "Directory with all alphabet images dosent exist"
    print "exiting..."
    sys.exit()

if os.path.isdir(r"./newMessage/"):
    print "Deleting existing 'newMessage' directory"
    shutil.rmtree(r"./newMessage/")
print "Creating new directory named newMessage"
os.mkdir(r"./newMessage/")

msg = input("Enter the new message ( Use quoates )( No numbers )" +
            "( max 42 char )\n")
msg = msg.lower().translate(None, "0123456789")
msg = (msg[:42] + '...') if len(msg) > 42 else msg

print "The entered message is: " + msg
i = 0
print "Creating message..."
for letter in msg:
    src = r"./alphabet/"+alpha_files[mapping[letter]]
    dst = r"./newMessage/" + a[i]
    shutil.copy(src, dst)
    i = i + 1
print "Go to './newMessage/' directory to see the message"
print "Completed"
