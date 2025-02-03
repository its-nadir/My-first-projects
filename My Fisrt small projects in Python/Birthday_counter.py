from datetime import datetime

now = datetime.now()
next_bday = datetime(now.year, 3, 16)

if next_bday < now:
    next_bday = next_bday.replace(year=now.year + 1)

diff = next_bday - now
days = diff.days

print(f"Remaining {days} days until your birthday")
#my
