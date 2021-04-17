def avr(ls): return sum(ls)/ len(ls)
def var(ls): return sum(map(lambda x: (x - avr(ls))**2 ,ls))

def tols(inp): return list(map(int, inp.split()))
def toout(rest): print("{:.2f}".format(rest))
def lsout(ls):
    print('[', end = "")
    for i in ls:
        print(i, end = " ")
    print(']', end = " ")

ls = sorted(tols(input()))
pos = dict(map(
  lambda x: (x,var(ls[:x])+ var(ls[x:])), 
  #find all (key, variance)
  range(1,len(ls))
  ))
minvar = min(pos.values())
toout(minvar)
print()
for i in pos:
    if(pos[i] == minvar):
        lsout(ls[:i])
        lsout(ls[i:])
        print()