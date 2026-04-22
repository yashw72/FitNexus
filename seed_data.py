import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'antigravity_project.settings')
django.setup()

from gym.models import MembershipPlan, Trainer, Member

if not MembershipPlan.objects.exists():
    p1 = MembershipPlan.objects.create(name='Basic Plan', duration_months=1, price=29.99)
    p2 = MembershipPlan.objects.create(name='Pro Plan', duration_months=6, price=149.99)
    p3 = MembershipPlan.objects.create(name='Elite Plan', duration_months=12, price=249.99)
    print("Plans created.")
else:
    p1 = MembershipPlan.objects.first()

if not Trainer.objects.exists():
    t1 = Trainer.objects.create(name='Arnold S.', specialty='Weightlifting', phone='555-0101')
    t2 = Trainer.objects.create(name='Serena W.', specialty='Cardio & Agility', phone='555-0102')
    print("Trainers created.")
else:
    t1 = Trainer.objects.first()

if not Member.objects.exists():
    Member.objects.create(first_name='Demo', last_name='User', email='demo@example.com', plan=p1, assigned_trainer=t1)
    print("Member created.")
