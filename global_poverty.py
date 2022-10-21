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