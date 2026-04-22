"""
seed_equipment.py — Seeds 25+ realistic gym equipment items into the database.
Run: python seed_equipment.py
"""
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'antigravity_project.settings')
django.setup()

from gym.models import Equipment
from datetime import date

equipment_data = [
    # ── Cardio ────────────────────────────────
    {"name": "Treadmill Pro X1",         "type": "Cardio",       "status": "Active",              "qty": 5, "location": "Cardio Zone",     "purchase": "2023-01-15", "maint": "2026-07-15"},
    {"name": "Elliptical Trainer",        "type": "Cardio",       "status": "Active",              "qty": 4, "location": "Cardio Zone",     "purchase": "2023-03-10", "maint": "2026-09-10"},
    {"name": "Stationary Bike",           "type": "Cardio",       "status": "Active",              "qty": 6, "location": "Cardio Zone",     "purchase": "2022-11-20", "maint": "2026-05-20"},
    {"name": "Rowing Machine",            "type": "Cardio",       "status": "Maintenance needed",  "qty": 2, "location": "Cardio Zone",     "purchase": "2022-06-05", "maint": "2026-04-20"},
    {"name": "Stair Climber",             "type": "Cardio",       "status": "Active",              "qty": 2, "location": "Cardio Zone",     "purchase": "2023-08-01", "maint": "2026-08-01"},
    {"name": "Air Bike (Assault)",        "type": "Cardio",       "status": "Active",              "qty": 3, "location": "Cardio Zone",     "purchase": "2024-01-10", "maint": "2026-07-10"},

    # ── Strength / Machines ─────────────────
    {"name": "Bench Press Station",       "type": "Strength",     "status": "Active",              "qty": 3, "location": "Weights Room",    "purchase": "2022-08-15", "maint": "2026-08-15"},
    {"name": "Squat Rack",                "type": "Strength",     "status": "Active",              "qty": 3, "location": "Weights Room",    "purchase": "2022-09-01", "maint": "2026-09-01"},
    {"name": "Deadlift Platform",         "type": "Strength",     "status": "Active",              "qty": 2, "location": "Weights Room",    "purchase": "2023-02-20", "maint": "2026-02-20"},
    {"name": "Cable Machine",             "type": "Strength",     "status": "Active",              "qty": 4, "location": "Weights Room",    "purchase": "2023-05-10", "maint": "2026-11-10"},
    {"name": "Leg Press Machine",         "type": "Strength",     "status": "Maintenance needed",  "qty": 2, "location": "Weights Room",    "purchase": "2021-12-05", "maint": "2026-04-30"},
    {"name": "Chest Fly Machine",         "type": "Strength",     "status": "Active",              "qty": 2, "location": "Weights Room",    "purchase": "2023-07-22", "maint": "2026-07-22"},
    {"name": "Lat Pulldown Machine",      "type": "Strength",     "status": "Active",              "qty": 2, "location": "Weights Room",    "purchase": "2023-06-14", "maint": "2026-06-14"},
    {"name": "Smith Machine",             "type": "Strength",     "status": "Active",              "qty": 2, "location": "Weights Room",    "purchase": "2023-04-01", "maint": "2026-10-01"},
    {"name": "Pec Deck Machine",          "type": "Strength",     "status": "Out of order",        "qty": 1, "location": "Weights Room",    "purchase": "2021-05-10", "maint": "2026-05-10"},

    # ── Free Weights ────────────────────────
    {"name": "Dumbbell Set (2–50 kg)",    "type": "Free Weights", "status": "Active",              "qty": 1, "location": "Free Weights Area","purchase": "2022-01-01", "maint": "2027-01-01"},
    {"name": "Olympic Barbell Set",       "type": "Free Weights", "status": "Active",              "qty": 10,"location": "Free Weights Area","purchase": "2022-01-01", "maint": "2027-01-01"},
    {"name": "Kettlebell Set (8–48 kg)",  "type": "Free Weights", "status": "Active",              "qty": 1, "location": "Free Weights Area","purchase": "2023-03-15", "maint": "2027-03-15"},
    {"name": "Weight Plates (5–25 kg)",   "type": "Free Weights", "status": "Active",              "qty": 60,"location": "Free Weights Area","purchase": "2022-01-01", "maint": "2027-01-01"},
    {"name": "EZ Curl Bar",               "type": "Free Weights", "status": "Active",              "qty": 4, "location": "Free Weights Area","purchase": "2022-04-10", "maint": "2027-04-10"},

    # ── Functional ──────────────────────────
    {"name": "Pull-up / Dip Station",     "type": "Functional",   "status": "Active",              "qty": 4, "location": "Functional Zone", "purchase": "2023-02-01", "maint": "2026-08-01"},
    {"name": "Battle Ropes (15m)",        "type": "Functional",   "status": "Active",              "qty": 3, "location": "Functional Zone", "purchase": "2023-06-20", "maint": "2026-12-20"},
    {"name": "TRX Suspension Trainer",    "type": "Functional",   "status": "Active",              "qty": 6, "location": "Functional Zone", "purchase": "2024-01-05", "maint": "2026-07-05"},
    {"name": "Plyo Box Set",              "type": "Functional",   "status": "Active",              "qty": 4, "location": "Functional Zone", "purchase": "2023-11-10", "maint": "2026-11-10"},
    {"name": "Medicine Ball Set",         "type": "Functional",   "status": "Active",              "qty": 1, "location": "Functional Zone", "purchase": "2023-09-01", "maint": "2026-09-01"},
    {"name": "Resistance Band Set",       "type": "Functional",   "status": "Active",              "qty": 10,"location": "Functional Zone", "purchase": "2024-02-14", "maint": "2026-08-14"},

    # ── Flexibility / Yoga ──────────────────
    {"name": "Yoga Mat",                  "type": "Flexibility",  "status": "Active",              "qty": 20,"location": "Yoga Studio",     "purchase": "2023-01-01", "maint": "2027-01-01"},
    {"name": "Foam Roller",               "type": "Flexibility",  "status": "Active",              "qty": 10,"location": "Recovery Zone",   "purchase": "2023-05-05", "maint": "2027-05-05"},
    {"name": "Stretching Pole Set",       "type": "Flexibility",  "status": "Active",              "qty":  5,"location": "Yoga Studio",     "purchase": "2024-01-20", "maint": "2027-01-20"},

    # ── Recovery ────────────────────────────
    {"name": "Massage Gun (Theragun Pro)","type": "Recovery",     "status": "Active",              "qty": 3, "location": "Recovery Zone",   "purchase": "2024-03-10", "maint": "2026-09-10"},
    {"name": "Ice Bath Tub",              "type": "Recovery",     "status": "Active",              "qty": 1, "location": "Recovery Zone",   "purchase": "2023-10-15", "maint": "2026-10-15"},
    {"name": "Compression Recovery Boots","type": "Recovery",     "status": "Maintenance needed",  "qty": 2, "location": "Recovery Zone",   "purchase": "2023-07-01", "maint": "2026-04-25"},
]

added = 0
skipped = 0

for item in equipment_data:
    if not Equipment.objects.filter(name=item["name"]).exists():
        Equipment.objects.create(
            name=item["name"],
            equipment_type=item["type"],
            status=item["status"],
            quantity=item["qty"],
            location=item["location"],
            purchase_date=item["purchase"],
            next_maintenance_date=item["maint"],
        )
        print(f"  [+] Added: {item['name']}")
        added += 1
    else:
        print(f"  [=] Skipped (exists): {item['name']}")
        skipped += 1

print(f"\n{'-'*50}")
print(f"Done! Added: {added}  |  Skipped: {skipped}  |  Total in DB: {Equipment.objects.count()}")
