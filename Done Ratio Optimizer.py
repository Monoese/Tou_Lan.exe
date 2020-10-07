from mip import Model, xsum, maximize, INTEGER
band_width = int(input("what is the total bandwidth for drones?: "))
model = Model()

d = [64, 32, 20]
b = [25, 10, 5]

n = {0, 1, 2}

x = [model.add_var(var_type=INTEGER) for i in n]

model.objective = maximize(xsum(d[i]*x[i] for i in n))

for i in n:
    model += xsum(x[i] for i in n) <= 5

for i in n:
    model += xsum(b[i]* x[i] for i in n) <= band_width

model.optimize()
print(x[0].x,'heavy',x[1].x,'medium',x[2].x,'light')