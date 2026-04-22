from django.contrib import admin
from .models import MembershipPlan, Trainer, Member, Equipment, Attendance

# Register your models here.
admin.site.register(MembershipPlan)
admin.site.register(Trainer)
admin.site.register(Member)
admin.site.register(Equipment)
admin.site.register(Attendance)
