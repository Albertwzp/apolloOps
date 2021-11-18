#! /bin/env python3

import re
pattern = r'\w+\d*\.(fat|dev|uat)\d\.\w+\.ws\.srv'
fd = open('/tmp/bmpl_fat5.txt')
txt =str(fd.readlines())
it = re.finditer(pattern, txt)
for sub in it:
    print(sub.group())
# with open('/tmp/properties.txt') as f:
#     prop = str(f.readlines())
#     #sub = pattern.findall(prop)
#     #print(sub)
