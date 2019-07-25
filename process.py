#!/usr/bin/python
import subprocess

#cp = subprocess.run(["ls", "-l"], stdout=subprocess.PIPE )
cp = subprocess.run(["add", "1", "2"], stdout=subprocess.PIPE )

print(cp.args)
print(cp.returncode)
#print(cp.stdout)

