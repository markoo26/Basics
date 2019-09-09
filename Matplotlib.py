##### LEGEND

###!### Comments to the code

##### IMPORT OF THE LIBRARIES #####


import numpy as np, pandas as pd, matplotlib.pyplot as plt
import matplotlib as mpl
import webbrowser

##### GO-TO #####

webbrowser.open_new_tab("https://matplotlib.org/tutorials/introductory/pyplot.html#sphx-glr-tutorials-introductory-pyplot-py")

##### USAGE GUIDE SECTION #####

fig = plt.figure()  ###!### An empty figure with no axes
fig.suptitle('No axes on this figure')  
fig, ax_lst = plt.subplots(2, 2)  ###!### Figure with 2x2 Axes

###!### All of plotting functions expect np.array or np.ma.masked_array as input
###!### Pandas DF and numpy matrix will therefore not work 

##### CONVERSION OF PD.DATAFRAME TO ACCEPTED DATATYPES #####

a = pd.DataFrame(np.random.rand(4,5), columns = list('abcde'))
a_asarray = a.values

b = np.matrix([[1,2],[3,4]])
b_asarray = np.asarray(b)

##### SIMPLE LINE CHARTS #####

x = np.linspace(0, 2, 100)

plt.plot(x, x, label='linear')
plt.plot(x, x**2, label='quadratic')
plt.plot(x, x**3, label='cubic')

plt.xlabel('x label')
plt.ylabel('y label')
plt.title("Simple Plot")
plt.legend()
plt.show()

##### TRIGONOMETRIC FUNCTIONS CHARTS #####

x = np.arange(-1, 1, 0.02)
y = np.arcsin(x)
fig, ax = plt.subplots()
ax.plot(x, y)
plt.show()

##### OWN PLOTTING FUNCTIONS #####

def my_plotter(ax, data1, data2, param_dict):
    out = ax.plot(data1, data2, **param_dict)
    return out

##### USING MY_PLOTTER WITH DIFFERENT MARKER TYPES #####
    
data1, data2, data3, data4 = np.random.randn(4, 100)
fig, ax = plt.subplots(1, 1)
my_plotter(ax, data1, data2, {'marker': 'x'})

fig, (ax1, ax2) = plt.subplots(1, 2)
my_plotter(ax1, data1, data2, {'marker': 'x'})
my_plotter(ax2, data3, data4, {'marker': 'o'})

###!### Different types of backend
###!### Interactive mode:

matplotlib.interactive() - to change cucrrent mode
matplotlib.is_interactive() - to check the current value

##### INTERACTIVE MODE #####

plt.ioff()
for i in range(3):
plt.plot(np.random.rand(10))
plt.show()

##### PERFORMANCE #####
##### path.simplify oraz path.simplify_threshold #####

mpl.rcParams['path.simplify'] = True
mpl.rcParams['path.simplify_threshold'] = 0.0 ## Default = 1/9

###!### agg.path.chunksize rc parameter 
###!### Chunk size - and any lines with greater than that many vertices 
###!### will be split into multiple lines

##### AUTOMATIC SETUP OF SIMPLICATION AND CHUNKING PARAMETERS #####

import matplotlib.style as mplstyle
mplstyle.use('fast')

##### PYPLOT TUTORIAL #####

import matplotlib.pyplot as plt
plt.plot([1, 2, 3, 4]) ###!###  0,1,2,3 are automatically assigned as X values
plt.ylabel('some numbers')
plt.show()

plt.plot([1, 2, 3, 4], [1, 4, 9, 16]) ###!### Adding X and Y axes

plt.plot([1, 2, 3, 4], [1, 4, 9, 16], 'ro') ###!### Chart type definition
plt.axis([0, 6, 0, 20])
plt.show()

##### THREE DIFFERENT CHART FORMATTING STYLES #####

t = np.arange(0., 5., 0.02)
plt.plot(t, t, 'r--', t, t**2, 'bs', t, t**3, 'g^')
plt.show()

##### SCATTERPLOT AND USING STRINGS AS ARGUMENT #####

data = {'a': np.arange(50),
        'c': np.random.randint(0, 50, 50),
        'd': np.random.randn(50)}
data['b'] = data['a'] + 10 * np.random.randn(50)
data['d'] = np.abs(data['d']) * 100

plt.scatter('a', 'b', c='c', s='d', data=data)
plt.xlabel('entry a')
plt.ylabel('entry b')
plt.show()

##### CHARTS WITH CATEGORICAL VARIABLES #####

names = ['group_a', 'group_b', 'group_c']
values = [1, 10, 100]

plt.figure(figsize=(9, 3))

plt.subplot(131)
plt.bar(names, values)
plt.subplot(132)
plt.scatter(names, values)
plt.subplot(133)
plt.plot(names, values)
plt.suptitle('Categorical Plotting')
plt.show()

##### CONTROLLING LINE PROPERTIES

plt.plot(x, y, linewidth=10.0)

line, = plt.plot(x, y, '-') ###!### TUPLE UNPACKING 
line.set_antialiased(False) ###!### TURN OFF ANTIALIASING

lines = plt.plot([1, 2, 3, 4], [1, 2, 3, 4], [11, 22, 33, 44], [1, 2, 3, 4])
plt.setp(lines, color='r', linewidth=22.0) ###!### USE KEYWORD ARGUMENTS

###!###  Available Line2D properties

plt.setp(lines) ###!### Attributes available to be edited in the chart

##### DEFINING ADVANCED TRIGONOMETRIC FUNCTIONS ##### 

def f(t):
    return np.exp(-t) * np.cos(2*np.pi*t)

t1 = np.arange(0.0, 5.0, 0.1)
t2 = np.arange(0.0, 5.0, 0.02)

plt.figure()
plt.subplot(211)
plt.plot(t1, f(t1), 'bo', t2, f(t2), 'k')

plt.subplot(212)
plt.plot(t2, np.cos(2*np.pi*t2), 'r--')
plt.show()


###!### The subplot() command specifies numrows, numcols, plot_number where 
###!###plot_number ranges from 1 to numrows*numcols.

###!### The commas in the subplot command are optional if numrows*numcols<10. 
###!### So subplot(211) is identical to subplot(2, 1, 1)

###!### clf() - clear figure, cla() - clear axes
###!### The memory required for a figure is not completely released until the 
###!### figure is explicitly closed with close().

###!### Plt.Text - adding a text box in described localisation ###!###

mu, sigma = 100, 15
x = mu + sigma * np.random.randn(10000)

##### HISTOGRAM OF THE DATA #####

n, bins, patches = plt.hist(x, 50, density=1, facecolor='g', alpha=0.75)
plt.xlabel('Smarts')
plt.ylabel('Probability')
plt.title('Histogram of IQ')
plt.text(60, .025, r'$\mu=100,\ \sigma=15$') ###!### Adding a text box
plt.axis([40, 160, 0, 0.03])
plt.grid(True)
plt.show()

##### MODIFICATION OF TEXT VALUES #####

t = plt.xlabel('my data', fontsize=14, color='red') 


##### TeX EXPRESSIONS IN TEXT BOX #####

plt.title(r'$\sigma_i=15$')
ax = plt.subplot(111)

t = np.arange(0.0, 5.0, 0.01)
s = np.cos(2*np.pi*t)
line, = plt.plot(t, s, lw=2)


##### USING PLT.ANNOTATE TO ADD ADNOTATIONS #####

plt.annotate('local max', xy=(2, 1), xytext=(3, 1.5),
             arrowprops=dict(facecolor='black', shrink=0.05),
             )

plt.ylim(-2, 2)
plt.show()