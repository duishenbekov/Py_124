import datetime
current_date = datetime.datetime.now().date()

# Добавляем 100 дней к текущей дате
future_date = current_date + datetime.timedelta(days=100)

print("Дата, которая наступит через 100 дней от текущей:", future_date)
