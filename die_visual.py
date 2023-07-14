from die import Die
from plotly.graph_objs import Bar, Layout
from plotly import offline

die_1 = Die()
die_2 = Die()

results = [die_1.roll() * die_2.roll() for i in range(1_000)]

#Analyse results
max_result = die_1.num_sides * die_2.num_sides 
frequencies = [results.count(i) for i in range(1, max_result+1)]
print(frequencies)

# Visualize the results.
x_values = list(range(1, max_result+1))
data = [Bar(x=x_values, y=frequencies)]

x_axis_config = {'title': 'Result', 'dtick': 1}
y_axis_config = {'title': 'Frequency of Result'}
my_layout = Layout(title='Results of multiplying a D6 and a D6 1000 times',
    xaxis=x_axis_config, yaxis=y_axis_config )  
offline.plot({'data': data, 'layout': my_layout}, filename='output\d6_d10.html')


