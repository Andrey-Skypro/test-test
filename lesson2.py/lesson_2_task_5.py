def month_to_season(month):
    if month in (3, 4, 5):
        return "Весна"
    elif month in (6, 7, 8):
        return "Лето"
    elif month in (9, 10, 11):
        return "Осень"
    elif month in (12, 1, 2):
        return "Зима"
    else:
        return "Недопустимый месяц"
month = 2
season = month_to_season(month)
print(season)
month = 54
season = month_to_season(month)
print(season)
