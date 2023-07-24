import matplotlib.pyplot as plt
from pandas import Series
from die import Die

die = Die()

results = [die.roll() for i in range(1000)]

#Analyse the results
frequencies = [results.count(i) for i in range(1, die.num_sides+1)]

#Visualise the results
x_vals = list(range(1,die.num_sides+1))
plt.bar(x_vals, frequencies)
plt.xlabel('Result')
plt.ylabel('Frequency of Result')
plt.title('Result of rolling a die 1000 times')

plt.show()

