url = 'https://docs.google.com/spreadsheets/d/1pQOYw2MQVrbrZqzv26NUmFL9P_PwXZ49/'

import pandas as pd
from datetime import date, timedelta

test = pd.read_excel(url + 'export?format=xlsx', header=1).dropna(axis=1, how='all')
test['Dates'] = pd.to_datetime(test['Dates'], errors='coerce')

def first_monday(year):
    first_monday = []
    for mes in range(1, 13):
        first_dia = date(year, mes, 1)
        while first_dia.weekday() != 0:
            first_dia += timedelta(days=1)
        first_monday.append(first_dia)
    return first_monday

mondays = first_monday(2025)

df_mondays = pd.DataFrame({
    'Dates': [fecha.strftime('%d-%m-%Y') for fecha in mondays]
})

test['Dates'] = test['Dates'].dt.strftime('%d-%m-%Y')

df = df_mondays.copy()
df['Answer Given'] = test['Dates']
df['Match'] = test['Dates'] == df['Dates']

print(df)