import re
import os
from fnmatch import fnmatch

root = os.path.dirname(os.path.realpath(__file__))
pattern = "*.txt"

for path, subdirs, files in os.walk(root):
    for name in files:
        if fnmatch(name, pattern):
            with open(path + "\\" + name, "r+") as fp:
                textfile = fp.read()
                x = re.search("owner = [A-Z][A-Z][A-Z]", textfile)
                if x is None:
                    fp.write("\nowner = CLN\ncontroller= CLN\n")


