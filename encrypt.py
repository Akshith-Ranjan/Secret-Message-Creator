#!/usr/bin/python

import os
import random
import shutil
import sys

if os.path.isdir(r"./encryptedMsg/"):
    print "Deleting existing encryptedMsg directory"
    shutil.rmtree(r"./encryptedMsg/")
print "Creating new directory named encryptedMsg"
os.mkdir(r"./encryptedMsg/")

if os.path.isdir(r"./newMessage/"):
    filenames = os.listdir(r"./newMessage/")
    if len(filenames) < 1:
        print "'newMessage' directory is empty. Run creator.py to create a message"
        print "Exiting..."
        sys.exit()
else:
    print "'newMessage' directory does not exist. Run creator.py to create a message"
    print "Exiting..."
    sys.exit()

for filename in filenames:
    src = r"./newMessage/"+filename
    dst = r"./encryptedMsg/" + str(random.randint(1, 30)) + filename
    shutil.copy(src, dst)
print "Completed encrypting"
