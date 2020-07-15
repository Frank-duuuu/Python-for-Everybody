# Finding Numbers in a Haystack
# In this assignment you will read through and parse a file with text and numbers.
# You will extract all the numbers in the file and compute the sum of the numbers.
# Note: Each student will have a distinct data file for the assignment - so only use your own data file for analysis.

import re
name = input('Enter file:')
if len(name) < 1:
    name = 'regex_sum_722225.txt'
handle = open(name)

num = list()
for line in handle:
    line = line.rstrip()
    read = re.findall('[0-9]+', line)
    for i in range(len(read)):
        num.append(int(read[i]))

print(sum(num))

# An alternative and more compacted way

import re
print(sum([int(num) for num in re.findall('[0-9]+', open('regex_sum_722225.txt').read())]))
