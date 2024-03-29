import matplotlib.pyplot as plt

input_values = [1,2,3,4,5]
squares = [1,4,9,16,25]

plt.style.use('seaborn')
fig,ax = plt.subplots()
ax.plot(input_values, squares, linewidth=3)

#Set chart title and label axes
ax.set_title("Square Numbers", fontsize=18)
ax.set_xlabel("Value", fontsize=12)
ax.set_ylabel("Square of Value", fontsize=12)

#Set size of tick labels
ax.tick_params(axis='both', labelsize=10)

plt.show()

