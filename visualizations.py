#run dataframes.py first

import pandas as pd
import datetime
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import matplotlib.cbook as cbook
from dataframes import *
from kind_datagather import *

#1

fig, ax = plt.subplots()
plt.title('Performance over the period')
ax2 = ax.twinx()

dfnew = df_fyc.reset_index().set_index('Year')
df_fpy.Polarity.plot(color='red', ax=ax2)
# dfnew.Year.plot.bar(color='None', edgecolor='red', hatch='/', ax=ax2)
dfnew.Count.plot.bar(color='blue', ax=ax)


ax.set_ylabel(ylabel='Count', color='blue')
ax.set_xlabel('Period')
ax2.set_ylabel("Polarity", color='red')
ax.legend(bbox_to_anchor=(1.1,1), loc="upper left")
ax2.legend(bbox_to_anchor=(1.1,0.9), loc="upper left")
ax.set_xticklabels(labels = [], rotation=90)
# plt.scatter(range(len(df_fpy['Year'])),df_fpy['Polarity'], color ='red', edgecolor='red', data = df_fpy)
fig.savefig('fig1.png')

plt.show()

#2

x = df_aa['Year']
y = df_aa['Polarity']


plt.close('all')

plt.figure(dpi=200)
# Just a figure and one subplot
f, ax = plt.subplots()
ax.scatter(x, y)
ax.set_title('Polarity Spots')
f.savefig('f.png')
# plt.show()

f1, ax1 = plt.subplots()
ax1.plot(df_aa_y['Year'], df_aa_y['Polarity'])
ax1.set_title('Average Polarity across Years')
f1.savefig('f1.png')
# plt.show()

f2, ax3 = plt.subplots()
ax3.scatter(x, y, color = 'red')
ax3.set_title('Polarity spots with Avg Polarity')
f2.savefig('f2.png')
# plt.show()

# f, ax1 = plt.subplots()
ax3.plot(df_aa_y['Year'], df_aa_y['Polarity'])
# ax2.set_title('Simple plot')
plt.savefig('3charts.png')
plt.show()

#3

from matplotlib.dates import MONDAY
from matplotlib.dates import MonthLocator, WeekdayLocator, DateFormatter

mondays = WeekdayLocator(MONDAY)
monthsFmt = DateFormatter("%b '%y")
months = MonthLocator(range(1, 13), bymonthday=1, interval=6)

dates = df_aa_fpd['Dates']
polarity = df_aa_fpd['Polarity']

plt.close('all')
fig, ax = plt.subplots()
ax.plot_date(dates, polarity, '-')
ax.xaxis.set_major_locator(months)
ax.xaxis.set_major_formatter(monthsFmt)
ax.xaxis.set_minor_locator(mondays)
ax.autoscale_view()
#ax.xaxis.grid(False, 'major')
#ax.xaxis.grid(True, 'minor')
ax.grid(True)
# ax.set_xticklabels(rotation=75)
fig.autofmt_xdate()
ax.set_title('Polarity curve across months')
plt.figure(dpi=100)
fig.savefig('pol.png')
plt.show()

#4

year = df_aa_fpd['Dates']
Polarity = df_aa_fpd['Polarity']

plt.close('all')
fig, ax = plt.subplots()
ax.plot_date(year, Polarity)
ax.grid(True)
plt.title('Polarity distribution based on Years')
plt.figure(dpi=100)
fig.savefig('s1.png')
plt.show()

#5

year = df_aa_fyc['Year']
count = df_aa_fyc['Count']


plt.close('all')
fig, ax = plt.subplots()
df_new_aa = df_aa_fyc.reset_index().set_index('Year')
df_new_aa.Count.plot.bar(color = 'red', ax=ax)
plt.title('Year v/s Count (review interests)')
plt.figure(dpi =100)
fig.savefig('yc.png')
plt.show()

#6

from matplotlib.dates import MONDAY
from matplotlib.dates import MonthLocator, WeekdayLocator, DateFormatter

mondays = WeekdayLocator(MONDAY)
monthsFmt = DateFormatter("%b '%y")
months = MonthLocator(range(1, 13), bymonthday=1, interval=6)

dates = df_fydp['Year']
polarity = df_fydp['Polarity']


plt.close('all')
fig, ax = plt.subplots()
# ax.plot_date(dates, polarity, '-')
# ax.xaxis.set_major_locator(months)
# ax.xaxis.set_major_formatter(monthsFmt)
# ax.xaxis.set_minor_locator(mondays)
# ax.autoscale_view()
# ax.plot(dates,polarity)
fydp = df_fydp.reset_index().set_index('Flavor')
fydp.Polarity.plot.bar(color='None', edgecolor='red', hatch='/', ax=ax)
# fydp.Y.plot(color = 'Red')
# ax.plot(df_fydp['Flavor'], polarity, color = 'red')
#ax.xaxis.grid(False, 'major')
#ax.xaxis.grid(True, 'minor')
# ax.grid(True)
# ax.set_xticklabels(rotation=75)
fig.autofmt_xdate()
ax.set_title('Polarity curve across months')
plt.show()

#7

fig, ax = plt.subplots()
plt.title('Performance over the period')
ax2 = ax.twinx()

x = range(len((df_fyc1['Count'])))
y = df_fyc1['Count']
f = df_fyc1['Flavor']

dfnew = df_fyc1.reset_index().set_index('Year')
df_fpy.Polarity.plot(color='red', ax=ax2)
dfnew.Count.plot.bar(color='blue', ax=ax)

ax.set_ylabel(ylabel='Count', color='blue')
ax.set_xlabel('Period')
ax2.set_ylabel("Polarity", color='red')
ax.legend(bbox_to_anchor=(1.1,1), loc="upper left")
ax2.legend(bbox_to_anchor=(1.1,0.9), loc="upper left")
ax.set_xticklabels(labels = [], rotation=90)
# plt.scatter(range(len(df_fpy['Year'])),df_fpy['Polarity'], color ='red', edgecolor='red', data = df_fpy)

plt.figure(dpi =100)
plt.show()

#8

# fig, ax = plt.subplots()
# dfnew.Count.plot.bar(color='blue', ax=ax)
# # plot.bar()
# plt.show()

col2 = ["pink", "green", "red", "blue", "orange", "black", "lime", "purple", "yellow", "indigo", "lightgreen",
        "darkred", "brown"]
x = range(len((dfnew['Flavor'])))
y = list(dfnew['Count'].astype(float))
z = np.arange(len(df_fpy['Flavor']))
f = list(dfnew['Flavor'])
for i in x:
    #     d = i%len(col1)
    d = list(df1['Flavor'].unique()).index(f[i])
    plt.bar(x[i], y[i], color=col2[d], label=str(df['Flavor'][d]))

    del d
# plt.legend(bbox_to_anchor=(1.0,1), loc="upper left")

# for col in range(len(col2)):
#     r = ax.bar(col)

rects1 = ax.bar(ind, yvals, width, color='pink')
rects2 = ax.bar(ind, yvals, width, color='green')
rects3 = ax.bar(ind, yvals, width, color='red')
rects4 = ax.bar(ind, yvals, width, color='blue')
rects5 = ax.bar(ind, yvals, width, color='orange')
rects6 = ax.bar(ind, yvals, width, color='black')
rects7 = ax.bar(ind, yvals, width, color='lime')
rects8 = ax.bar(ind, yvals, width, color='purple')
rects9 = ax.bar(ind, yvals, width, color='yellow')
rects10 = ax.bar(ind, yvals, width, color='indigo')
rects11 = ax.bar(ind, yvals, width, color='brown')
rects12 = ax.bar(ind, yvals, width, color='lightgreen')
rects13 = ax.bar(ind, yvals, width, color='maroon')

plt.legend((rects1[0], rects2[0], rects3[0], rects4[0], rects5[0], rects6[0], rects7[0], rects8[0], rects9[0],
            rects10[0], rects11[0], rects12[0], rects13[0]), str(df1['Flavor'].unique()), bbox_to_anchor=(1.0, 1),
           loc="upper left")
# ax.set_xticklabels(labels = dfnew.index, rotation=75)
plt.title('Count of exp instances for Year-wise-Flavor groups')
plt.savefig('colors.png', dpi=100)
plt.show()

#9

col1 = ["blue", "green", "red", "blue", "orange", "black", "orange", "black", "orange", "black", "black", "orange",
        "green"]
x = range(len((df_fpy['Flavor'])))
y = df_fpy['Polarity']
z = np.arange(len(df_fpy['Flavor']))
f = df_fpy['Flavor']
for i in x:
    #     d = i%len(col1)
    d = list(df1['Flavor'].unique()).index(f[i])
    plt.bar(x[i], y[i], color=col1[d], label=str(df_fpy['Flavor'][i]))

    del d
# plt.legend(bbox_to_anchor=(1.0,1), loc="upper left")
plt.savefig()
plt.title('Polarity distribution for each index')
plt.figure(dpi=100)
plt.savefigure('pdeach.png')
plt.show()

#10

fig, ax = plt.subplots()
plt.title('Performance over the period')
# ax2 = ax.twinx()

# dfnew = df_aa.reset_index().set_index('Dates')
# dfnew.Polarity.plot(color='blue', ax=ax)
# dfnew.Year.plot.bar(color='None', edgecolor='red', hatch='/', ax=ax2)
# dfnew.Count.plot.bar(color='blue', ax=ax)


# ax.set_ylabel(ylabel='Count', color='blue')
# ax.set_xlabel('Period')
# ax2.set_ylabel("Polarity", color='red')
# ax.legend(bbox_to_anchor=(1.1,1), loc="upper left")
# ax2.legend(bbox_to_anchor=(1.1,0.9), loc="upper left")
# ax.set_xticklabels(labels = d, rotation=90)
plt.scatter(range(len(df_aa['Year'])),df_aa['Polarity'], edgecolor='red')
plt.savefig('scttr.png')

plt.show()