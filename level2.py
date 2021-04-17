def avr(ls): return sum(ls)/ len(ls)
def var(ls): return sum(map(lambda x: (x - avr(ls))**2 ,ls))

def tols(inp): return list(map(int, inp.split()))
def toout(rest): print("{:.2f}".format(rest))


ls = sorted(tols(input()) + tols(input()))

toout(var(ls[:len(ls)//2])+ var(ls[len(ls)//2:]))