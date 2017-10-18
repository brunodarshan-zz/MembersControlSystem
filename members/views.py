from django.shortcuts import render, redirect,get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Member, Instituition, Position, Actuation, Specialty
from .forms import MemberForm, InstituitionForm, PositionForm, ActuationForm, SpecialtyForm


@login_required(login_url='/')
def dashboard(request):
	return render(request, '/dashboard.html')


@login_required(login_url='/')
def members_list(request):
	members = Member.objects.all().order_by('id')
	return render(request, 'members/index.html', {'members' : members})


@login_required(login_url='/')
def instituitions_list(request):
	instituitions = Instituition.objects.all().order_by('id')
	return render(request, 'instituitions/index.html', {'instituitions' : instituitions})


@login_required(login_url='/')
def positions_list(request):
	positions = Position.objects.all().order_by('id')
	return render(request, 'positions/index.html', {'positions' : positions})


@login_required(login_url='/')
def actuations_list(request):
	actuations = Actuation.objects.all().order_by('id')
	return render(request, 'actuations/index.html', {'actuations' : actuations})


@login_required(login_url='/')
def specialties_list(request):
	specialties = Specialty.objects.all().order_by('id')
	return render(request, 'specialties/index.html', {'specialties' : specialties})


@login_required(login_url='/')
def add_member(request):
	if request.method == "POST":
		form = MemberForm(request.POST)

		if form.is_valid():
			member = form.save()

			return redirect('members_list')

	else:
		form = MemberForm()

	return render(request, 'members/add.html', {'form' : form})


@login_required(login_url='/')
def add_instituition(request):
	if request.method == "POST":
		form = InstituitionForm(request.POST)

		if form.is_valid():
			instituition = form.save()

			return redirect('instituitions_list')

	else:
		form = InstituitionForm()

	return render(request, 'instituition/add.html', {'form' : form})


@login_required(login_url='/')
def add_position(request):
	if request.method == "POST":
		form = PositionForm(request.POST)

		if form.is_valid():
			position = form.save()

			return redirect('positions_list')

	else:
		form = PositionForm()

	return render(request, 'position/add.html', {'form' : form})


@login_required(login_url='/')
def add_actuation(request):
	if request.method == "POST":
		form = ActuationForm(request.POST)

		if form.is_valid():
			actuation = form.save()

			return redirect('actuations_list')

	else:
		form = ActuationForm()

	return render(request, 'actuation/add.html', {'form' : form})


@login_required(login_url='/')
def add_specialty(request):
	if request.method == "POST":
		form = SpecialtyForm(request.POST)

		if form.is_valid():
			specialty = form.save()

			return redirect('specialties_list')

	else:
		form = SpecialtyForm()

	return render(request, 'specialty/add.html', {'form' : form})


@login_required(login_url='/')
def add_extras(request):
	return render(request, 'extras/add.html')


@login_required(login_url='/')
def view_extras(request):
	return render(request, 'extras/show.html')


def about(request):
	return render(request, '/about.html')


@login_required(login_url='/')
def member_remove(request, pk):
	member = get_object_or_404(Member, pk=pk)
	member.delete()
	return redirect('members_list')


@login_required(login_url='/')
def instituition_remove(request, pk):
	instituition = get_object_or_404(Instituition, pk=pk)
	instituition.delete()
	return redirect('instituitions_list')


@login_required(login_url='/')
def position_remove(request, pk):
	position = get_object_or_404(Position, pk=pk)
	position.delete()
	return redirect('positions_list')


@login_required(login_url='/')
def actuation_remove(request, pk):
	actuation = get_object_or_404(Actuation, pk=pk)
	actuation.delete()
	return redirect('actuations_list')


@login_required(login_url='/')
def specialty_remove(request, pk):
	specialty = get_object_or_404(Specialty, pk=pk)
	specialty.delete()
	return redirect('specialties_list')


@login_required(login_url='/')
def member_edit(request, pk):
	member = get_object_or_404(Member, pk=pk)

	if request.method == "POST":
		form = MemberForm(request.POST, instance=member)

		if form.is_valid():
			member.save()

			return redirect('members_list')

	else:
		form = MemberForm()

	return render(request, 'members/add.html', {'form' : form})


@login_required(login_url='/')
def instituition_edit(request, pk):
	instituition = get_object_or_404(Instituition, pk=pk)

	if request.method == "POST":
		form = InstituitionForm(request.POST, instance=instituition)

		if form.is_valid():
			instituition.save()

			return redirect('instituitions_list')

	else:
		form = InstituitionForm()

	return render(request, 'instituition/add.html', {'form' : form})


@login_required(login_url='/')
def position_edit(request, pk):
	position = get_object_or_404(Position, pk=pk)

	if request.method == "POST":
		form = PositionForm(request.POST, instance=position)

		if form.is_valid():
			position.save()

			return redirect('positions_list')

	else:
		form = PositionForm()

	return render(request, 'position/add.html', {'form' : form})


@login_required(login_url='/')
def actuation_edit(request, pk):
	actuation = get_object_or_404(Actuation, pk=pk)

	if request.method == "POST":
		form = ActuationForm(request.POST, instance=actuation)

		if form.is_valid():
			actuation.save()

			return redirect('actuations_list')

	else:
		form = ActuationForm()

	return render(request, 'actuation/add.html', {'form' : form})


@login_required(login_url='/')
def specialty_edit(request, pk):
	specialty = get_object_or_404(Specialty, pk=pk)

	if request.method == "POST":
		form = SpecialtyForm(request.POST, instance=specialty)

		if form.is_valid():
			specialty.save()
			return redirect('specialties_list')

	else:
		form = SpecialtyForm()

	return render(request, 'specialty/add.html', {'form' : form})


@login_required(login_url='/')
def member_detail(request, pk):
	member = get_object_or_404(Member, pk=pk)
	return render(request, 'members/show.html', {'member' : member})
