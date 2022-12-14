from pyjstat import pyjstat
import requests
import os
import json
from datetime import datetime
import locale
import io
import pandas as pd
os.makedirs('data', exist_ok=True)

#Extreme Poverty Share World
df_csv = pd.read_csv('https://api.worldbank.org/pip/v1/pip-grp?country=WLD&year=all&group_by=wb&format=csv')
df_new = df_csv.pivot(index='reporting_year', columns='region_name', values='headcount')*100
df_new.to_csv('data/Extreme_Poverty_World_Share.csv', index=True)

#Extreme Poverty Population World
df_csv = pd.read_csv('https://api.worldbank.org/pip/v1/pip-grp?country=WLD&year=all&group_by=wb&format=csv')
df_new = df_csv.pivot(index='reporting_year', columns='region_name', values='pop_in_poverty')
df_new.to_csv('data/Extreme_Poverty_World_Population.csv', index=True)

#Extreme Poverty Share Region
df_csv = pd.read_csv('https://api.worldbank.org/pip/v1/pip-grp?country=all&year=all&group_by=wb&format=csv')
df_new = df_csv.pivot(index='reporting_year', columns='region_name', values='headcount')*100
df_new.drop(['World'], axis=1,inplace=True)
df_new.to_csv('data/Extreme_Poverty_Regions_Share.csv', index=True)

#Extreme Poverty Population Region
df_csv = pd.read_csv('https://api.worldbank.org/pip/v1/pip-grp?country=all&year=all&group_by=wb&format=csv')
df_new = df_csv.pivot(index='reporting_year', columns='region_name', values='pop_in_poverty')
df_new.drop(['World'], axis=1,inplace=True)
df_new.to_csv('data/Extreme_Poverty_Regions_Population.csv', index=True)

#Extreme Poverty Share Country
df_csv = pd.read_csv('https://api.worldbank.org/pip/v1/pip?country=all&year=all&povline=2.15&fill_gaps=false&reporting_level=all&format=csv')
df_new = df_csv.sort_values('reporting_year').groupby('country_name').tail(1)
df_new['headcount'] = df_new['headcount']*100
df_new2 = df_new[['country_name', 'reporting_year', 'headcount']]
df_new3 = df_new2[df_new2['reporting_year'] > 2005]
df_new3.to_csv('data/Extreme_Poverty_Country_Share.csv', index=True)

#Extreme Poverty Country Profile
df_csv = pd.read_csv('https://api.worldbank.org/pip/v1/pip?country=all&year=all&povline=2.15&fill_gaps=false&reporting_level=all&format=csv')
df_new = df_csv.sort_values('reporting_year').groupby('country_name').tail(1)
df_new['pop_in_poverty'] = df_new['headcount']*df_new['reporting_pop']
df_new['headcount'] = df_new['headcount']*100
df_new2 = df_new[['country_name', 'reporting_year', 'headcount', 'pop_in_poverty']]
df_new3 = df_new2[df_new2['reporting_year'] > 2005]
df_new3.to_csv('data/Extreme_Poverty_Country_Profile.csv', index=True)