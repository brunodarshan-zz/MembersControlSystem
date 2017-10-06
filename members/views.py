from django.shortcuts import render, redirect,get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Member, Instituition, Position, Actuation, Specialty
from .forms import MemberForm, InstituitionForm, PositionForm, ActuationForm, SpecialtyForm


@login_required
def dashboard(request):
	return render(request, 'members/dashboard.html')


@login_required
def members_list(request):
	members = Member.objects.all().order_by('id')
	return render(request, 'members/members_list.html', {'members' : members})


@login_required
def instituitions_list(request):
	instituitions = Instituition.objects.all().order_by('id')
	return render(request, 'members/instituitions_list.html', {'instituitions' : instituitions})


@login_required
def positions_list(request):
	positions = Position.objects.all().order_by('id')
	return render(request, 'members/positions_list.html', {'positions' : positions})


@login_required
def actuations_list(request):
	actuations = Actuation.objects.all().order_by('id')
	return render(request, 'members/actuations_list.html', {'actuations' : actuations})


@login_required
def specialties_list(request):
	specialties = Specialty.objects.all().order_by('id')
	return render(request, 'members/specialties_list.html', {'specialties' : specialties})


@login_required
def add_member(request):
	if request.method == "POST":
		form = MemberForm(request.POST)

		if form.is_valid():
			member = form.save()

			return redirect('members_list')

	else:
		form = MemberForm()

	return render(request, 'members/add_member.html', {'form' : form})


@login_required
def add_instituition(request):
	if request.method == "POST":
		form = InstituitionForm(request.POST)

		if form.is_valid():
			instituition = form.save()

			return redirect('instituitions_list')

	else:
		form = InstituitionForm()

	return render(request, 'members/add_instituition.html', {'form' : form})


@login_required
def add_position(request):
	if request.method == "POST":
		form = PositionForm(request.POST)

		if form.is_valid():
			position = form.save()

			return redirect('positions_list')

	else:
		form = PositionForm()

	return render(request, 'members/add_position.html', {'form' : form})


@login_required
def add_actuation(request):
	if request.method == "POST":
		form = ActuationForm(request.POST)

		if form.is_valid():
			actuation = form.save()

			return redirect('actuations_list')

	else:
		form = ActuationForm()

	return render(request, 'members/add_actuation.html', {'form' : form})


@login_required
def add_specialty(request):
	if request.method == "POST":
		form = SpecialtyForm(request.POST)

		if form.is_valid():
			specialty = form.save()

			return redirect('specialties_list')

	else:
		form = SpecialtyForm()

	return render(request, 'members/add_specialty.html', {'form' : form})


@login_required
def add_extras(request):
	return render(request, 'members/add_extras.html')


@login_required
def view_extras(request):
	return render(request, 'members/view_extras.html')


def about(request):
	return render(request, 'members/about.html')


@login_required
def member_remove(request, pk):
	member = get_object_or_404(Member, pk=pk)
	member.delete()
	return redirect('members_list')


@login_required
def instituition_remove(request, pk):
	instituition = get_object_or_404(Instituition, pk=pk)
	instituition.delete()
	return redirect('instituitions_list')


@login_required
def position_remove(request, pk):
	position = get_object_or_404(Position, pk=pk)
	position.delete()
	return redirect('positions_list')


@login_required
def actuation_remove(request, pk):
	actuation = get_object_or_404(Actuation, pk=pk)
	actuation.delete()
	return redirect('actuations_list')


@login_required
def specialty_remove(request, pk):
	specialty = get_object_or_404(Specialty, pk=pk)
	specialty.delete()
	return redirect('specialties_list')


@login_required
def member_edit(request, pk):
	member = get_object_or_404(Member, pk=pk)

	if request.method == "POST":
		form = MemberForm(request.POST, instance=member)

		if form.is_valid():
			member.save()

			return redirect('members_list')

	else:
		form = MemberForm()

	return render(request, 'members/add_member.html', {'form' : form})


@login_required
def instituition_edit(request, pk):
	instituition = get_object_or_404(Instituition, pk=pk)

	if request.method == "POST":
		form = InstituitionForm(request.POST, instance=instituition)

		if form.is_valid():
			instituition.save()

			return redirect('instituitions_list')

	else:
		form = InstituitionForm()

	return render(request, 'members/add_instituition.html', {'form' : form})


@login_required
def position_edit(request, pk):
	position = get_object_or_404(Position, pk=pk)

	if request.method == "POST":
		form = PositionForm(request.POST, instance=position)

		if form.is_valid():
			position.save()

			return redirect('positions_list')

	else:
		form = PositionForm()

	return render(request, 'members/add_position.html', {'form' : form})


@login_required
def actuation_edit(request, pk):
	actuation = get_object_or_404(Actuation, pk=pk)

	if request.method == "POST":
		form = ActuationForm(request.POST, instance=actuation)

		if form.is_valid():
			actuation.save()

			return redirect('actuations_list')

	else:
		form = ActuationForm()

	return render(request, 'members/add_actuation.html', {'form' : form})


@login_required
def specialty_edit(request, pk):
	specialty = get_object_or_404(Specialty, pk=pk)

	if request.method == "POST":
		form = SpecialtyForm(request.POST, instance=specialty)

		if form.is_valid():
			specialty.save()

			return redirect('specialties_list')

	else:
		form = SpecialtyForm()

	return render(request, 'members/add_specialty.html', {'form' : form})


@login_required
def member_detail(request, pk):
	member = get_object_or_404(Member, pk=pk)
	return render(request, 'members/member_detail.html', {'member' : member})