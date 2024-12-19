import plotly.express as px
from dice import Dice

# Create a D6 and a D10
dice_1 = Dice(8)
dice_2 = Dice(8)

# Make some rolls, and store results in a list.
results = []
for roll in range(1_000):
    result = dice_1.roll() + dice_2.roll()
    results.append(result)

# Analyze the results.
frequencies = []
max_results = dice_1.num_sides + dice_2.num_sides
poss_results = range(2, max_results+1)
for value in poss_results:
    frequency = results.count(value)
    frequencies.append(frequency)

# Visualize the results.
title = "Results of Rolling a Two D8 1,000 Times"
labels = {'x':'Results', 'y':'Frequency of Result'}
fig = px.bar(x=poss_results, y=frequencies, title=title, labels=labels)

# Further customize chart.
fig.update_layout(xaxis_dtick=1)

# fig.write_html('dice_visual_d6d10.html')
fig.show()