import os 

def run(cmd):
    os.system(cmd)

def chdir(path):
    os.chdir(path)

run('apt install git')
run('adduser git')
chdir('/home/git')
run('git init --bare gzq_linux.git')
run('chown -R git:git gzq_linux.git')

#禁止登陆
run('mv /etc/passwd /etc/passwd.bak')
run('touch /etc/passwd')
with open('/etc/passwd.bak', 'r') as r:
    with open('/etc/passwd', 'w') as w:
        for i in r.readlines():
            s = i.split(':')
            if s[0] != 'git':
                w.write('%s\n' % i)
            else:
                s[-1] = '/home/git:/usr/bin/git-shell'
                w.write(':'.join(s))

print('git clone ssh://git@ip:port/home/git/gzq_linux.git')
