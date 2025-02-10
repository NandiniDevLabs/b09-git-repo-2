from datetime import datetime
import os

print("This is first line of home.py")
print(datetime.now())

# Should complete this code
# Requirment: Read all the content from data/input/ directory

filenames = os.listdir('data/input/')
contents = []
for filename in filenames:
    print(f"Reading content from file: {filename}")
    with open('data/input/'+filename) as file:
        contents.append(file.read())
#

print("========================")
print(contents)
print("========================")