import os
from os import listdir
from os.path import isfile, join
import re

DIRNAME = './scripts'

file_name_valid = re.compile('^\d{5}.*\.sql')

only_files = [f for f in listdir(DIRNAME) if isfile(join(DIRNAME, f))]

success_files = [f for f in only_files if file_name_valid.match(f)]
fail_files = [f for f in only_files if not file_name_valid.match(f)]

success_numbers = [int(f[0:5]) for f in success_files]

print(only_files)
print(success_files)
print(fail_files)

if not success_files:
    next_number = 1
else:
    next_number = max(success_numbers) + 1

for f in fail_files:
    number_string = f"{next_number:05d}c-"
    os.rename(join(DIRNAME, f), join(DIRNAME, number_string+f))
print(only_files)
print(success_files)
print(fail_files)
