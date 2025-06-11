# Date-Calculation
- 🌟 Every Other Day Excel and Power Query Challenges No247🌟 * Author: Omid Motamedisedeh
 
    - Topic: Date Calculation!
 
 🔰 Generate the dates of the first Monday of each month in 2025.
 
 🔗 Link to Excel file:
 👉 https://lnkd.in/dTsKB4bG

**My code in Python** 🐍 **for this challenge**
```
from datetime import date, timedelta

def first_monday(year):
    first_monday = []
    for mes in range(1, 13):
        first_dia = date(year, mes, 1)
        while first_dia.weekday() != 0:
            first_dia += timedelta(days=1)
        first_monday.append(first_dia)
    return first_monday

for monday in first_monday(2025):
    print(monday.strftime("%d-%m-%Y"))
```
## Output :
```
06-01-2025
03-02-2025
03-03-2025
07-04-2025
05-05-2025
02-06-2025
07-07-2025
04-08-2025
01-09-2025
06-10-2025
03-11-2025
01-12-2025
```
