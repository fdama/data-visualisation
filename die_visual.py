from die import Die
from plotly.graph_objs import Bar, Layout
from plotly import offline

die = Die()

results = [die.roll() for i in range(1000)]

#Analyse results
frequencies = [results.count(i) for i in range(1, die.num_sides+1)]
print(frequencies)

# Visualize the results.
x_values = list(range(1, die.num_sides+1))
data = [Bar(x=x_values, y=frequencies)]

x_axis_config = {'title' : 'Result'}
y_axis_config = {'title' : 'Frequency of Result'}
my_layout = Layout(title='Results of rolling one D6 1000 times',
    xaxis=x_axis_config, yaxis=y_axis_config )  
offline.plot({'data': data, 'layout': my_layout}, filename='output\d6.html')


