import pandas as pd
from kind_datagather import *
from visualizations import *

df = df.reset_index(drop=True)

from dateutil import parser
dates_list = []
for each in df['Dates']:
    dates_list.append(parser.parse(each).strftime('%Y-%m-%d'))

dates_year = []
for each in df['Dates']:
    dates_year.append(parser.parse(each).strftime('%Y'))

df1 = pandas.DataFrame(columns = ['Flavor', 'Polarity'])
df1['Flavor'] = df['Flavor']
df1['Dates'] = dates_list
df1['Polarity'] = df['Polarity']
df1['Year'] = dates_year

df_fp = pandas.DataFrame(columns = ['Flavor','Polarity'], dtype = float)

df_fp['Polarity'] = df['Polarity'].apply(pandas.to_numeric)
df_fp['Flavor'] = df['Flavor']

df_fp.groupby(['Flavor']).mean().reset_index()

df_fpy = pandas.DataFrame(columns = ['Flavor','Polarity','Year'], dtype = float)
df_fpy['Polarity'] = df['Polarity'].apply(pandas.to_numeric)
df_fpy['Flavor'] = df['Flavor']
df_fpy['Year'] = dates_year

df_fpy.groupby(['Year']).mean().reset_index()

df_fpy['Year'].unique()

df_fpy.groupby(['Year','Flavor']).mean().reset_index()

df_fyc = df_fpy.groupby(['Flavor','Year']).size().reset_index()
df_fyc.columns = ['Flavor','Year','Count']

df_aa = df_fpy.loc[df_fpy['Flavor'] == 'Flavor: Almonds & Apricots in Yogurt|Size: Pack of 12']
# .apply(pandas.to_numeric)

df_aa = df_aa.sort_values(['Year'])
# df_aa['Dates'] = df1['Dates'].loc[df1['Flavor'] == 'Flavor: Almonds & Apricots in Yogurt|Size: Pack of 12']

df_aa_y = df_aa.groupby(['Flavor','Year']).mean().reset_index()

df_aa_fpd = df1.loc[df1['Flavor'] == 'Flavor: Almonds & Apricots in Yogurt|Size: Pack of 12']

df_aa_fpd = df_aa_fpd.sort_values(['Dates'])

df_aa.groupby(['Flavor','Year']).mean().reset_index()

df_aa_fyc = df_aa.groupby(['Year']).size().reset_index()
df_aa_fyc.columns = ['Year', 'Count']

df_fydp = df1.groupby(['Flavor','Year','Dates']).mean().reset_index()

df_fyc1 = df_fyc.groupby(['Year','Flavor']).mean().reset_index()

