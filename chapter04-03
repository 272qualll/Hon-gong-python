#Number of base codons
base = input("please enter the base sequence : ")
n_base = [base[i:i+3] for i in range(0,len(base),3)]
d_base = {}

for k in n_base:
    if len(k) != 3:
        continue
    if k not in d_base:
        d_base[k] = 0
    d_base[k] += 1
    
print(d_base)
