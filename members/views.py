from django.shortcuts import render, redirect,get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Member, Instituition, Position, Actuation, Specialty
from .forms import MemberForm, InstituitionForm, PositionForm, ActuationForm, SpecialtyForm

def dashboard(request):
	return render(request, 'members/dashboard.html')


def members_list(request):
	members = Member.objects.all().order_by('id')
	return render(request, 'members/members_list.html', {'members' : members})


def instituitions_list(request):
	instituitions = Instituition.objects.all().order_by('id')
	return render(request, 'members/instituitions_list.html', {'instituitions' : instituitions})


def positions_list(request):
	positions = Position.objects.all().order_by('id')
	return render(request, 'members/positions_list.html', {'positions' : positions})


def actuations_list(request):
	actuations = Actuation.objects.all().order_by('id')
	return render(request, 'members/actuations_list.html', {'actuations' : actuations})


def specialties_list(request):
	specialties = Specialty.objects.all().order_by('id')
	return render(request, 'members/specialties_list.html', {'specialties' : specialties})


def add_member(request):
	if request.method == "POST":
		form = MemberForm(request.POST)

		if form.is_valid():
			member = form.save()

			return redirect('members_list')

	else:
		form = MemberForm()

	return render(request, 'members/add_member.html', {'form' : form})


def add_instituition(request):
	if request.method == "POST":
		form = InstituitionForm(request.POST)

		if form.is_valid():
			instituition = form.save()

			return redirect('instituitions_list')

	else:
		form = InstituitionForm()

	return render(request, 'members/add_instituition.html', {'form' : form})


def add_position(request):
	if request.method == "POST":
		form = PositionForm(request.POST)

		if form.is_valid():
			position = form.save()

			return redirect('positions_list')

	else:
		form = PositionForm()

	return render(request, 'members/add_position.html', {'form' : form})


def add_actuation(request):
	if request.method == "POST":
		form = ActuationForm(request.POST)

		if form.is_valid():
			actuation = form.save()

			return redirect('actuations_list')

	else:
		form = ActuationForm()

	return render(request, 'members/add_actuation.html', {'form' : form})


def add_specialty(request):
	if request.method == "POST":
		form = SpecialtyForm(request.POST)

		if form.is_valid():
			specialty = form.save()

			return redirect('specialties_list')

	else:
		form = SpecialtyForm()

	return render(request, 'members/add_specialty.html', {'form' : form})


def add_extras(request):
	return render(request, 'members/add_extras.html')


def view_extras(request):
	return render(request, 'members/view_extras.html')


def about(request):
	return render(request, 'members/about.html')