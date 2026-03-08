from datetime import datetime

def get_days_from_today(date):
    try:
        user_date = datetime.strptime(date, '%Y-%m-%d').date()
    except ValueError:
        return None
    today = datetime.today().date()
    return (today - user_date).days

