from pwn import *
from subprocess import *
context.log_level = 'DEBUG'

p=remote('203.66.14.26',31337)
out = subprocess.Popen(['hashcash', '-mb24', 'lufimqgb'],
                       stdout=subprocess.PIPE,
                       stderr=subprocess.STDOUT)
stdout, stderr = out.communicate()
# print(str(stdout))
# res = str(stdout).split(' ')[2]
p.sendline(str(stdout))
p.interactive()
