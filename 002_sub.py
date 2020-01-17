import re

txt = "W środku nocy, PRZYMIOTNIK, zgrabna RZECZOWNIK CZASOWNIK na RZECZOWNIK i sikała."
replacements = ['PRZYMIOTNIK', 'RZECZOWNIK', 'CZASOWNIK', 'RZECZOWNIK']

lst = []
for val in replacements:
    user_val = input(f'{val}: ')
    pair = (val, user_val)
    lst.append(pair)


for old, new in lst:
    txt = re.sub(old, new, txt, 1)

print(txt)