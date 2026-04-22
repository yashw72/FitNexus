from gym.models import Member, Equipment, Attendance
import datetime
from django.utils import timezone

# Equipment
Equipment.objects.get_or_create(name='Treadmill T-1000', equipment_type='Cardio', status='Active', purchase_date=datetime.date(2025, 1, 15))
Equipment.objects.get_or_create(name='Bench Press Pro', equipment_type='Strength', status='Active', purchase_date=datetime.date(2025, 2, 10))
Equipment.objects.get_or_create(name='Rowing Machine X', equipment_type='Cardio', status='Out of order', purchase_date=datetime.date(2024, 11, 5))
Equipment.objects.get_or_create(name='Leg Extension Master', equipment_type='Strength', status='Maintenance needed', purchase_date=datetime.date(2025, 3, 20))

# Attendance
member = Member.objects.first()
if member:
    for i in range(5):
        try:
            date = timezone.now().date() - datetime.timedelta(days=i)
            check_in = datetime.time(8, 0, 0)
            check_out = datetime.time(9, 30, 0)
            Attendance.objects.get_or_create(member=member, date=date, check_in_time=check_in, check_out_time=check_out)
        except Exception as e:
            pass

print("Seed successful")
