def avr(ls): return sum(ls)/ len(ls)
def var(ls): return sum(map(lambda x: (x - avr(ls))**2 ,ls))

def tols(inp): return list(map(int, inp.split()))

rest = var(tols(input()))
print("{:.2f}".format(rest))