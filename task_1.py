import re

# Исходная строка с временными значениями
time_string = '1h 45m,360s,25m,30m 120s,2h 60s'

# Разделяем строку на отдельные временные значения
time_values = time_string.split(',')

# Переменная для хранения общего количества минут
total_minutes = 0

# Обрабатываем каждое временное значение
for value in time_values:
    # Убираем лишние пробелы
    value = value.replace(' ', '')
    
    # Используем регулярные выражения для поиска часов, минут и секунд
    hours_match = re.search(r'(\d+)h', value)
    minutes_match = re.search(r'(\d+)m', value)
    seconds_match = re.search(r'(\d+)s', value)

    # Если найдены часы, добавляем их в минуты
    if hours_match:
        hours = int(hours_match.group(1))
        total_minutes += hours * 60

    # Если найдены минуты, добавляем их в общее количество минут
    if minutes_match:
        minutes = int(minutes_match.group(1))
        total_minutes += minutes

    # Если найдены секунды, добавляем их в минуты (60 секунд = 1 минута)
    if seconds_match:
        seconds = int(seconds_match.group(1))
        total_minutes += seconds // 60

# Выводим общее количество минут
print("Общее количество минут:", total_minutes)