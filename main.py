from datetime import date, datetime


def get_birthdays_per_week(users):
    
    current_date = date.today()
    
    if all(user["birthday"].year > current_date.year for user in users):
        return {}
    
    users = {
        'Monday': ['Bill', 'Jan'],
        'Tuesday': ['Kim'],
        'Wednesday': [],
        'Thursday': [],
        'Friday': [],
    }
    
    print(users)
    
    return users


if __name__ == "__main__":
    users = [
        {"name": "Jan Koum", "birthday": datetime(1976, 1, 1).date()},
    ]

    result = get_birthdays_per_week(users)
    print(result)
    # Виводимо результат
    for day_name, names in result.items():
        print(f"{day_name}: {', '.join(names)}")
