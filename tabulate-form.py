from collections import defaultdict
from tabulate import tabulate
import itertools
import csv
import re
import sys

times_regex = '(\d+\.\d+\.\d+, \d+:\d+, \w+)'

reader = csv.reader(sys.stdin)
data = [i for i in reader][1:]

res = defaultdict(list)

times = set()

for i in data:
    for w in re.findall(times_regex, i[2]):
        times.add(w)

times = list(times)
times.sort()

for i in data:
    who = i[1]
    when = re.findall(times_regex, i[2])
    
    for w in times:
        res[w].append(who if w in when else '')

cols = [[i] + res[i] for i in res]
print(tabulate(itertools.zip_longest(*cols, fillvalue='')))
