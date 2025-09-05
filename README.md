# Date-Calculation
- 🌟 Every Other Day Excel and Power Query Challenges No247🌟 * Author: Omid Motamedisedeh
 
  ## Topic: Date Calculation!
    - Calcula el primer lunes de cada mes en el año que elijas.
    - Carga fechas desde un archivo Excel.
    - Compara si las fechas dadas coinciden con las esperadas.
    - Devuelve un DataFrame con el resultado.
 
 🔰 Generate the dates of the first Monday of each month in 2025. 📅
 
 🔗 Link to Excel file:
 👉 https://lnkd.in/dTsKB4bG

**My code in Python** 🐍 **for this challenge**

```python
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
```
## Output :

```
       Dates   Answer Given  Match
0   06-01-2025   06-01-2025   True
1   03-02-2025   03-02-2025   True
2   03-03-2025   03-03-2025   True
3   07-04-2025   07-04-2025   True
4   05-05-2025   05-05-2025   True
5   02-06-2025   02-06-2025   True
6   07-07-2025   07-07-2025   True
7   04-08-2025   04-08-2025   True
8   01-09-2025   01-09-2025   True
9   06-10-2025   06-10-2025   True
10  03-11-2025   03-11-2025   True
11  01-12-2025   01-12-2025   True
```

## ⚒ Requisitos
```bash
pip install pandas openpyxl
```
## 🚀 Ejecución
```python
date_calculation.py
```
