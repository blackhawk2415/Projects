import matplotlib.pyplot as plt


x = []
y = []

x2 = []
y2 = []

output = []
output2 = []


fig = plt.figure()
box = fig.patch
box.set_facecolor('grey')


# box = fig.patch
# box.set_facecolor('#31312e')


with open('data.txt', 'r') as file:
	output = file.read().split('\n')

with open('data2.txt', 'r') as file:
	output2 = file.read().split('\n')


for plot in output:
	coordinates = plot.split(',')
	x.append(int(coordinates[0]))
	y.append(int(coordinates[1]))

for plot2 in output2:
	coordinates2 = plot2.split(',')
	x2.append(int(coordinates2[0]))
	y2.append(int(coordinates2[1]))


graph1 = fig.add_subplot(2,2,1, axisbg='grey')
graph1.plot(x, y, 'c', linewidth=2.5)

# styles

graph1.tick_params(axis='x', colors='b')
graph1.tick_params(axis='y', colors='w')
graph1.spines['bottom'].set_color('w')
graph1.set_title('Graph 1', color='white')
graph1.set_xlabel('x axis')
graph1.set_ylabel('y axis')


graph2 = fig.add_subplot(2,2,2, axisbg='black')
graph2.plot(x2, y2, 'cyan', linewidth=2.5)

plt.show()





