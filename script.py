import subprocess

out = subprocess.check_output(
    'git -C ../steven-rummler.github.io log --no-merges --stat=100000,8192')

lines = out.decode('ascii').split('\n')

print(len(lines))
