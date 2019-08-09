import glob
import os

path_source = glob.glob('*.py')

path_target = glob.glob('*.py')

path_source = [path for path in path_source]
path_target = [path for path in path_target]


num = 0
for path in path_source:
	if path in path_target:
		print(path)
		num += 1

print(num)