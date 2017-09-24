import os
import sys

fileName = sys.argv[1]

fileSize = os.path.getsize(fileName)
print (fileSize)