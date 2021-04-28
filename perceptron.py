import time
import matplotlib as mpl
mpl.use('TkAgg')
import matplotlib.pyplot as plt

A = (0, 6)
B = (1, 5)
C = (3, 3)
D = (2, 4)
P = 4
delta = 0.1
niter = 500
deadline = 5  # seconds

dots = (A, B, C, D)
exp_res = (1, 1, 6, 6)   # A<P, B<P, C>P, D>P
curr_res = [0, 0, 0, 0]

w1 = 0; w2 = 0
a = [0, 0, 0, 0]
empty_iter = 0

t_start = time.time()
x = 0
for i in range(niter):
    a[x] += 1
    curr_res[x] = w1*dots[x][0] + w2*dots[x][1]

    if (curr_res[x] > P and exp_res[x] > P) or (curr_res[x] < P and exp_res[x] < P):
        empty_iter +=1
        pass;
    else:
        empty_iter = 0
        w_delta = P - curr_res[x]
        w1 = w1 + w_delta * dots[x][0] * delta
        w2 = w2 + w_delta * dots[x][1] * delta

    if empty_iter > 10:
        print(i)
        break
    if time.time()-t_start > deadline:
        print("deadline")
        break

    if x != 3: x += 1
    else: x = 0


print(curr_res)
print(a)
print("w1 = {}\nw2 = {}".format(w1, w2))

#show plot
plt.switch_backend('TkAgg')

fig = plt.figure()
mpl.rcParams.update({'font.size': 10})

ax1 = fig.add_subplot(111)

plt.ylim(-10, 10)
x = range(0, 6)
y = [(P-i*w1)/w2 for i in x]

ax1.plot(x, y, color='blue', linestyle='solid')

x1 = [i[0] for i in dots]
y1 = [i[1] for i in dots]
ax1.plot(x1, y1, 'rx')

plt.show()
