#the number of bases
base = input("please enter the base sequence : ")
n_base = {}

for k in base:
    if k not in n_base:
        n_base[k] = 0
    n_base[k] += 1
    
for l in n_base:
    print("number of {} : {}".format(l, n_base[l]))
