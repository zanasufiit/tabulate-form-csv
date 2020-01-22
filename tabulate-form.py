from collections import defaultdict
from tabulate import tabulate
import itertools
import csv
import re
import sys

reader = csv.reader(sys.stdin)
data = [i for i in reader][1:-3]

res = defaultdict(list)
for i in data:
    who = i[1]
    when = re.findall('(\d+\.\d+\.\d+, \d+:\d+, \w+)', i[2])
    
    for w in when:
        res[w].append(who)


cols = [[i] + res[i] for i in res]

max_cnt = max((len(i) for i in cols))

print(tabulate(itertools.zip_longest(*cols, fillvalue='')))
