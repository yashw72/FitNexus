from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Q
from datetime import date

from .models import Member, Trainer, MembershipPlan, Equipment, Attendance


# ─── Auth ────────────────────────────────────────────────────────────────────

def login_view(request):
    if request.user.is_authenticated:
        return redirect('home')
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            messages.success(request, f'Welcome back, {user.username}!')
            return redirect('home')
        else:
            messages.error(request, 'Invalid username or password. Please try again.')
    return render(request, 'gym/login.html')


def logout_view(request):
    logout(request)
    messages.info(request, 'You have been logged out.')
    return redirect('login')


# ─── Dashboard ───────────────────────────────────────────────────────────────

@login_required
def home(request):
    total_members = Member.objects.count()
    total_trainers = Trainer.objects.count()
    total_equipment = Equipment.objects.count()
    today_attendance = Attendance.objects.filter(date=date.today()).count()
    maintenance_count = Equipment.objects.filter(status='Maintenance needed').count()
    out_of_order = Equipment.objects.filter(status='Out of order').count()

    # Revenue estimate: sum of plan prices for all members with plans
    revenue = sum(
        m.plan.price for m in Member.objects.select_related('plan').all() if m.plan
    )

    recent_attendance = Attendance.objects.select_related('member').order_by(
        '-date', '-check_in_time'
    )[:5]

    context = {
        'total_members': total_members,
        'total_trainers': total_trainers,
        'total_equipment': total_equipment,
        'today_attendance': today_attendance,
        'maintenance_count': maintenance_count,
        'out_of_order': out_of_order,
        'revenue': revenue,
        'recent_attendance': recent_attendance,
    }
    return render(request, 'gym/home.html', context)


# ─── Members ─────────────────────────────────────────────────────────────────

@login_required
def member_list(request):
    search = request.GET.get('search', '')
    members = Member.objects.select_related('plan', 'assigned_trainer').all()
    if search:
        members = members.filter(
            Q(first_name__icontains=search) | Q(last_name__icontains=search) | Q(email__icontains=search)
        )
    return render(request, 'gym/members.html', {'members': members, 'search': search})


@login_required
def add_member(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        gender = request.POST.get('gender')
        email = request.POST.get('email')
        phone = request.POST.get('phone', '')
        plan_id = request.POST.get('plan')
        trainer_id = request.POST.get('trainer')

        # Check for duplicate email
        if Member.objects.filter(email=email).exists():
            messages.error(request, f'❌ A member with the email "{email}" is already registered.')
            plans = MembershipPlan.objects.all()
            trainers = Trainer.objects.all()
            return render(request, 'gym/add_member.html', {
                'plans': plans, 
                'trainers': trainers,
                'form_data': request.POST
            })

        plan = MembershipPlan.objects.filter(id=plan_id).first() if plan_id else None
        trainer = Trainer.objects.filter(id=trainer_id).first() if trainer_id else None

        Member.objects.create(
            first_name=first_name,
            last_name=last_name,
            gender=gender,
            email=email,
            phone=phone,
            plan=plan,
            assigned_trainer=trainer
        )
        messages.success(request, f'✅ Member {first_name} {last_name} registered successfully!')
        return redirect('members')

    plans = MembershipPlan.objects.all()
    trainers = Trainer.objects.all()
    return render(request, 'gym/add_member.html', {'plans': plans, 'trainers': trainers})


@login_required
def delete_member(request, member_id):
    member = get_object_or_404(Member, id=member_id)
    if request.method == 'POST':
        name = str(member)
        member.delete()
        messages.success(request, f'🗑️ Member {name} has been removed.')
        return redirect('members')
    return redirect('members')


# ─── Trainers ────────────────────────────────────────────────────────────────

@login_required
def trainers_list(request):
    trainers = Trainer.objects.all()
    return render(request, 'gym/trainers.html', {'trainers': trainers})


@login_required
def add_trainer(request):
    if not request.user.is_staff:
        messages.error(request, '⛔ Only admins can add trainers.')
        return redirect('trainers')
    if request.method == 'POST':
        name = request.POST.get('name')
        specialty = request.POST.get('specialty')
        phone = request.POST.get('phone')
        email = request.POST.get('email', '')
        try:
            experience_years = int(request.POST.get('experience_years', 1))
        except (ValueError, TypeError):
            messages.error(request, '❌ Experience years must be a number.')
            return render(request, 'gym/add_trainer.html', {'form_data': request.POST})

        Trainer.objects.create(
            name=name,
            specialty=specialty,
            phone=phone,
            email=email,
            experience_years=experience_years,
        )
        messages.success(request, f'✅ Trainer {name} added successfully!')
        return redirect('trainers')
    return render(request, 'gym/add_trainer.html')


@login_required
def delete_trainer(request, trainer_id):
    if not request.user.is_staff:
        messages.error(request, '⛔ Only admins can delete trainers.')
        return redirect('trainers')
    trainer = get_object_or_404(Trainer, id=trainer_id)
    if request.method == 'POST':
        name = trainer.name
        trainer.delete()
        messages.success(request, f'🗑️ Trainer {name} has been removed.')
        return redirect('trainers')
    return redirect('trainers')


# ─── Plans ───────────────────────────────────────────────────────────────────

@login_required
def plans_list(request):
    plans = MembershipPlan.objects.all()
    return render(request, 'gym/plans.html', {'plans': plans})


# ─── Equipment ───────────────────────────────────────────────────────────────

@login_required
def equipment_list(request):
    equipment = Equipment.objects.all()
    search_q = request.GET.get('search', '')
    type_filter = request.GET.get('type', '')
    status_filter = request.GET.get('status', '')

    if search_q:
        equipment = equipment.filter(name__icontains=search_q)
    if type_filter:
        equipment = equipment.filter(equipment_type=type_filter)
    if status_filter:
        equipment = equipment.filter(status=status_filter)

    all_types = Equipment.objects.values_list('equipment_type', flat=True).distinct().order_by('equipment_type')
    active_count = Equipment.objects.filter(status='Active').count()
    maintenance_count = Equipment.objects.filter(status='Maintenance needed').count()
    broken_count = Equipment.objects.filter(status='Out of order').count()

    context = {
        'equipment': equipment,
        'all_types': all_types,
        'search_q': search_q,
        'selected_type': type_filter,
        'selected_status': status_filter,
        'active_count': active_count,
        'maintenance_count': maintenance_count,
        'broken_count': broken_count,
    }
    return render(request, 'gym/equipment.html', context)


@login_required
def add_equipment(request):
    if not request.user.is_staff:
        messages.error(request, '⛔ Only admins can add equipment.')
        return redirect('equipment')
    if request.method == 'POST':
        Equipment.objects.create(
            name=request.POST.get('name'),
            equipment_type=request.POST.get('equipment_type'),
            status=request.POST.get('status', 'Active'),
            quantity=int(request.POST.get('quantity') or 1),
            location=request.POST.get('location', 'Main Floor'),
            purchase_date=request.POST.get('purchase_date') or None,
            next_maintenance_date=request.POST.get('next_maintenance_date') or None,
        )
        messages.success(request, '✅ Equipment added successfully!')
        return redirect('equipment')
    return render(request, 'gym/add_equipment.html')


@login_required
def update_equipment_status(request, equipment_id):
    if not request.user.is_staff:
        messages.error(request, '⛔ Only admins can update equipment status.')
        return redirect('equipment')
    item = get_object_or_404(Equipment, id=equipment_id)
    if request.method == 'POST':
        item.status = request.POST.get('status')
        item.save()
        messages.success(request, f'✅ {item.name} status updated to "{item.status}".')
    return redirect('equipment')


@login_required
def delete_equipment(request, equipment_id):
    if not request.user.is_staff:
        messages.error(request, '⛔ Only admins can delete equipment.')
        return redirect('equipment')
    item = get_object_or_404(Equipment, id=equipment_id)
    if request.method == 'POST':
        name = item.name
        item.delete()
        messages.success(request, f'🗑️ Equipment {name} removed from inventory.')
    return redirect('equipment')


# ─── Attendance ──────────────────────────────────────────────────────────────

@login_required
def attendance_list(request):
    attendance_records = Attendance.objects.select_related('member').order_by('-date', '-check_in_time')
    date_filter = request.GET.get('date', '')
    member_search = request.GET.get('member', '')

    if date_filter:
        attendance_records = attendance_records.filter(date=date_filter)
    if member_search:
        attendance_records = attendance_records.filter(
            Q(member__first_name__icontains=member_search) |
            Q(member__last_name__icontains=member_search)
        )

    today = date.today()
    today_count = Attendance.objects.filter(date=today).count()
    present_count = Attendance.objects.filter(date=today, status='Present').count()
    late_count = Attendance.objects.filter(date=today, status='Late').count()
    absent_count = Attendance.objects.filter(date=today, status='Absent').count()

    context = {
        'attendance_records': attendance_records,
        'members': Member.objects.order_by('first_name', 'last_name'),
        'today_count': today_count,
        'present_count': present_count,
        'late_count': late_count,
        'absent_count': absent_count,
        'date_filter': date_filter,
        'member_search': member_search,
        'today': today,
    }
    return render(request, 'gym/attendance.html', context)


@login_required
def mark_attendance(request):
    if request.method == 'POST':
        member_id = request.POST.get('member_id')
        status = request.POST.get('status', 'Present')
        member = get_object_or_404(Member, id=member_id)
        today = date.today()

        # Prevent duplicate attendance for same day
        existing = Attendance.objects.filter(member=member, date=today).first()
        if existing:
            messages.warning(request, f'⚠️ Attendance for {member} already marked today ({existing.status}).')
        else:
            now = timezone.localtime(timezone.now()).time()
            Attendance.objects.create(
                member=member,
                date=today,
                check_in_time=now,
                status=status,
            )
            messages.success(request, f'✅ {status} marked for {member} at {now.strftime("%I:%M %p")}.')
    return redirect('attendance')


@login_required
def checkout_member(request, attendance_id):
    record = get_object_or_404(Attendance, id=attendance_id)
    if request.method == 'POST':
        now = timezone.localtime(timezone.now()).time()
        record.check_out_time = now
        record.save()
        messages.success(request, f'✅ Check-out recorded for {record.member} at {now.strftime("%I:%M %p")}.')
    return redirect('attendance')
