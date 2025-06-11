# Date-Calculation
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
