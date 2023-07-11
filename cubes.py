import matplotlib.pyplot as plt

x_nums = range(1,5001)
y_nums = [n**3 for n in x_nums]
#print(y_nums)

fig,ax = plt.subplots()
ax.plot(x_nums, y_nums)

ax.set_title("Cubed Numbers", fontsize=18)
ax.set_xlabel("Value", fontsize=10)
ax.set_ylabel("Cube of Value", fontsize=10)

print(max(x_nums), max(y_nums))
ax.axis([0, max(x_nums), 0, max(y_nums)])
ax.tick_params(axis='both', which='major', labelsize=14)


plt.show()