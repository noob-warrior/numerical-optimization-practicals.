import pulp as p
LPP= p.LpProblem('PROBLEM', p.LpMinimize)
x = p.LpVariable("x", lowBound=0)
y = p.LpVariable("y", lowBound=0)
LPP+= 3 * x + 5 * y
LPP+= 2 * x + 3 * y >= 12
LPP+= -x + y <=3
LPP+= x>=4
LPP+= y<=3

print(LPP)
status= LPP.solve()
print(p.LpStatus[status])
print(p.value(x), p.value(y), p.value(LPP.objective))
