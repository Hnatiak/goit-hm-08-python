from datetime import date, datetime

def get_birthdays_per_week(users):
    current_date = date.today()
    birthday_dict = {}
    
    for user in users:
        year = current_date.year + 1 if (current_date.month == 12 and current_date.day > 24) and user["birthday"].month == 1 else current_date.year
        birthday = datetime(year, user["birthday"].month, user["birthday"].day).date()
        
        if 0 <= (birthday - current_date).days < 7:
            
            weekday = birthday.strftime("%A")
            if weekday == 'Saturday' or weekday == 'Sunday':
                weekday = 'Monday'
                
            name = user["name"].split()[0]
            
            if weekday in birthday_dict.keys():
                birthday_dict[weekday].append(name)
            else:
                birthday_dict[weekday] = [name]
                
    print(birthday_dict)
    return birthday_dict



if __name__ == "__main__":
    users = [
        {"name": "Jan Koum", "birthday": datetime(1976, 1, 1).date()},
    ]

    result = get_birthdays_per_week(users)
    print(result)
    # Виводимо результат
    for day_name, names in result.items():
        print(f"{day_name}: {', '.join(names)}")
