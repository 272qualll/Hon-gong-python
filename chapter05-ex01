#pibonacci sequence / taking notes
'''
Before taking notes: the recursive function of this code must be recalculated from scratch, 
even if it is once obtained.

def pibonacci(a):
    if a == 1:
        return 1
    if a == 2:
        return 1
    else:     
        return pibonacci(a-1) + pibonacci(a-2)
'''
# after taking notes
def pibonacci(a):
    if a in memo:
        return memo[a]
    else:
        output = pibonacci(a-1) + pibonacci(a-2)
        memo[a] = output
        return output

memo = {1 : 1, 2 : 1}
        
print(pibonacci(1))
print(pibonacci(2))
print(pibonacci(5))
