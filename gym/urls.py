from django.urls import path
from . import views

urlpatterns = [
    # Dashboard
    path('', views.home, name='home'),

    # Members
    path('members/', views.member_list, name='members'),
    path('add-member/', views.add_member, name='add_member'),
    path('delete-member/<int:member_id>/', views.delete_member, name='delete_member'),

    # Trainers
    path('trainers/', views.trainers_list, name='trainers'),
    path('add-trainer/', views.add_trainer, name='add_trainer'),
    path('delete-trainer/<int:trainer_id>/', views.delete_trainer, name='delete_trainer'),

    # Plans
    path('plans/', views.plans_list, name='plans'),

    # Equipment
    path('equipment/', views.equipment_list, name='equipment'),
    path('add-equipment/', views.add_equipment, name='add_equipment'),
    path('update-equipment-status/<int:equipment_id>/', views.update_equipment_status, name='update_equipment_status'),
    path('delete-equipment/<int:equipment_id>/', views.delete_equipment, name='delete_equipment'),

    # Attendance
    path('attendance/', views.attendance_list, name='attendance'),
    path('mark-attendance/', views.mark_attendance, name='mark_attendance'),
    path('checkout/<int:attendance_id>/', views.checkout_member, name='checkout_member'),
]
