### fcont.py
### COMSC 175, Nwagbogu Jack
### January 27, 2025
### Time taken = 10 mins


any_list = ['23', 'hello', 'keyano', 'college', '10', 'jack', '12']
nlist = []
for i in any_list:
    try:
        nlist.append(float(i))
    except ValueError:
        continue
if len(nlist) > 0:
    avg_list = sum(nlist) / len(nlist)
else:
    avg_list =  0
print('nlist:', nlist)
print('Average of nlist:', avg_list)
