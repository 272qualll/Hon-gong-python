#flattening list of Recursive function

def flatten(li):
    n_li = []
    for k in li:
        if type(k) != list:
            n_li.append(k)
        else:
            n_li += flatten(k)
    return n_li
    
ex = [1,2,3,[4,[5,6,[7,8]]],9]

print("original : ", ex)
print("Conversion : ", flatten(ex))
