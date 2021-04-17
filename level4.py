from itertools import combinations

def avr(ls): return sum(ls)/ len(ls)
def var(ls): return sum(map(lambda x: (x - avr(ls))**2 ,ls))
lsvar = lambda ls: sum(map(var,ls))

def tols(inp): return list(map(int, inp.split()))
def toout(rest): print("{:.2f}".format(rest), end = " ")
def lsout(ls):
    print('[', end = "")
    for i in ls:
        print(i, end = " ")
    print(']', end = " ")

def allout(ls):
    for i in ls:
        if type(i) == list:
            lsout(i)

def decomp(ls, l):
    l = [0] + l + [len(ls)]
    rest = []
    for i in range(len(l)-1):
      rest.append(ls[l[i]: l[i+1]])
    return rest

m = int(input()) - 1
l = tols(input())
n = len(l)
ls = list(range(1,m+1))

pos =  {} 
for seq in combinations(l[:-1], m):
    pos[seq] = lsvar(decomp(l,list(seq)))

minvar = min(pos.values())
toout(minvar)
print()
for seq in pos:
    if(pos[seq] == minvar):
        allout(decomp(l,list(seq)))
        print()