from django.db import models
from datetime import date


class MembershipPlan(models.Model):
    name = models.CharField(max_length=100)
    duration_months = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.name} ({self.duration_months} months)"


class Trainer(models.Model):
    name = models.CharField(max_length=100)
    specialty = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    email = models.EmailField(blank=True, default='')
    experience_years = models.IntegerField(default=1)

    def __str__(self):
        return self.name


class Member(models.Model):
    GENDER_CHOICES = [('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other')]
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES, default='Male')
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=20, blank=True, default='')
    plan = models.ForeignKey(MembershipPlan, on_delete=models.SET_NULL, null=True)
    assigned_trainer = models.ForeignKey(Trainer, on_delete=models.SET_NULL, null=True, blank=True)
    join_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Equipment(models.Model):
    STATUS_CHOICES = [
        ('Active', 'Active'),
        ('Maintenance needed', 'Maintenance needed'),
        ('Out of order', 'Out of order'),
    ]
    name = models.CharField(max_length=100)
    equipment_type = models.CharField(max_length=50)
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, default='Active')
    quantity = models.IntegerField(default=1)
    location = models.CharField(max_length=100, blank=True, default='Main Floor')
    purchase_date = models.DateField(null=True, blank=True)
    next_maintenance_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return f"{self.name} - {self.status}"


class Attendance(models.Model):
    STATUS_CHOICES = [
        ('Present', 'Present'),
        ('Late', 'Late'),
        ('Absent', 'Absent'),
    ]
    member = models.ForeignKey(Member, on_delete=models.CASCADE)
    date = models.DateField(default=date.today)
    check_in_time = models.TimeField(null=True, blank=True)
    check_out_time = models.TimeField(null=True, blank=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Present')

    class Meta:
        ordering = ['-date', '-check_in_time']

    def __str__(self):
        return f"{self.member} - {self.date} ({self.status})"
