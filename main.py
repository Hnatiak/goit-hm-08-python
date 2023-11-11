from datetime import date, datetime

def get_birthdays_per_week(users):
    current_date = date.today()
    current_weekday = current_date.weekday()

    if all(user["birthday"].year > current_date.year for user in users):
        return {}

    weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    birthdays_per_week = {day: [] for day in weekdays}

    for user in users:
        birthday = user["birthday"]
        diff = (birthday.replace(year=current_date.year) - current_date).days
        next_birthday_weekday = (current_weekday + diff) % 7
        day_name = weekdays[next_birthday_weekday]
        birthdays_per_week[day_name].append(user["name"])

    return birthdays_per_week

if __name__ == "__main":
    users = [
        {"name": "Jan Koum", "birthday": datetime(1976, 1, 1).date()},
    ]

    result = get_birthdays_per_week(users)

    # Print the result
    for day_name, names in result.items():
        print(f"{day_name}: {', '.join(names)}")














# from datetime import date, datetime

# def get_birthdays_per_week(users):
    
#     current_date = date.today()
#     current_weekday = current_date.weekday()
    
#     if all(user["birthday"].year > current_date.year for user in users):
#         return {}
    
#     for user in users:
#         birthday = user["birthday"]
#         diff = (birthday - current_date).days
#         next_birthday_weekday = (current_weekday + diff) % 7
#         day_name = list(users.keys())[next_birthday_weekday]
#         users[day_name].append(user["name"])
    
#     return users
    
#     # birthdays_per_week = {
#     #     'Monday': ['Bill', 'Jan'],
#     #     'Tuesday': ['Kim'],
#     #     'Wednesday': [],
#     #     'Thursday': [],
#     #     'Friday': [],
#     # }
    
#     # print(users)
    
#     # for day, names in users.items():
#     #     birthdays_per_week[day] = [name for name in names if name in users[day]]
    
#     # return birthdays_per_week


# if __name__ == "__main__":
#     users = [
#         {"name": "Jan Koum", "birthday": datetime(1976, 1, 1).date()},
#     ]

#     result = get_birthdays_per_week(users)
#     print(result)
#     # Виводимо результат
#     for day_name, names in result.items():
#         print(f"{day_name}: {', '.join(names)}")





















# from datetime import date, timedelta

# def get_birthdays_per_week(users):
#     # Сьогоднішня дата
#     today = date.today()

#     # Список днів тижня в порядку
#     days_of_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

#     # Створюємо словник для збереження днів народження
#     birthdays_per_week = {day: [] for day in days_of_week}

#     # Проходимося по користувачам і додаємо їх до словника, якщо їх день народження в цьому тижні
#     for user in users:
#         user_name = user['name']
#         user_birthday = user['birthday']

#         # Обчислюємо день тижня для дня народження користувача
#         birthday_weekday = user_birthday.weekday()

#         # Визначаємо різницю в днях між сьогоднішньою датою і днем народження
#         days_until_birthday = (user_birthday - today).days

#         # Перевіряємо, чи день народження в цьому тижні і чи не минув вже цього року
#         if 0 <= birthday_weekday < 5 and days_until_birthday >= 0:
#             # Додаємо користувача до відповідного дня тижня
#             birthdays_per_week[days_of_week[birthday_weekday]].append(user_name)

#     # Переносимо дні народження, якщо вони випадають на вихідні (Saturday, Sunday)
#     for day in ["Saturday", "Sunday"]:
#         birthdays_per_week["Monday"].extend(birthdays_per_week[day])
#         birthdays_per_week[day] = []

#     return birthdays_per_week

# # Приклад використання:
# if __name__ == "__main__":
#     users = [
#         {"name": "Bill", "birthday": date(2023, 11, 14)},
#         {"name": "Jan", "birthday": date(2023, 11, 16)},
#         {"name": "Kim", "birthday": date(2023, 11, 15)},
#         {"name": "DIED", "birthday": date(1980, 11, 15)},
#         {"name": "ROMAN", "birthday": date(2024, 11, 15)},
#         {"name": "OLEG", "birthday": date(2026, 9, 15)},
#     ]

#     birthdays = get_birthdays_per_week(users)
#     print(birthdays)

