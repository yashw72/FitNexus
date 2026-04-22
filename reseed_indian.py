import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'antigravity_project.settings')
django.setup()

from gym.models import MembershipPlan, Trainer, Member

Member.objects.all().delete()
Trainer.objects.all().delete()
MembershipPlan.objects.all().delete()

p1 = MembershipPlan.objects.create(name='Basic Plan', duration_months=1, price=999.00)
p2 = MembershipPlan.objects.create(name='Pro Plan', duration_months=6, price=4999.00)
p3 = MembershipPlan.objects.create(name='Elite Plan', duration_months=12, price=8999.00)
print("Plans created.")

t1 = Trainer.objects.create(name='Rajesh Kumar', specialty='Weightlifting', phone='+91 98765 43210')
t2 = Trainer.objects.create(name='Priya Sharma', specialty='Yoga & Aerobics', phone='+91 87654 32109')
t3 = Trainer.objects.create(name='Vikram Singh', specialty='CrossFit', phone='+91 76543 21098')
print("Trainers created.")

Member.objects.create(first_name='Rahul', last_name='Verma', gender='Male', email='rahul.verma@example.com', plan=p1, assigned_trainer=t1)
Member.objects.create(first_name='Ananya', last_name='Patel', gender='Female', email='ananya.p@example.com', plan=p2, assigned_trainer=t2)
print("Members created.")
