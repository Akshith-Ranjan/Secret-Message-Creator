#!/usr/bin/python

import os
import shutil
import sys

if os.path.isdir(r"./decryptedMsg/"):
    print "Deleting existing encryptedMsg directory"
    shutil.rmtree(r"./decryptedMsg/")
print "Creating new directory named decryptedMsg"
os.mkdir(r"./decryptedMsg/")

if os.path.isdir(r"./encryptedMsg/"):
    filenames = os.listdir(r"./encryptedMsg/")
    if len(filenames) < 1:
        print "'encryptedMsg' directory is empty. Run encrypt.py to create an encrypted message"
        print "Exiting..."
        sys.exit()
else:
    print "'encryptedMsg' directory does not exist. Run encrypt.py to create a message"
    print "Exiting..."
    sys.exit()

for filename in filenames:
    src = r"./encryptedMsg/"+filename
    dst = r"./decryptedMsg/" + filename.translate(None,"0123456789")
    shutil.copy(src, dst)
print "Completed decrypting"
