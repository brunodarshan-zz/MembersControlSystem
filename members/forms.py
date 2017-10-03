# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from django import forms
from .models import Member, Instituition, Position, Actuation, Specialty


class MemberForm(forms.ModelForm):
	class Meta:
		model = Member
		fields = ('name', 'cpf', 'rg', 'position', 'instituition', 'actuations', 'contact', 'specialties', 'student_ifpi', 'matriculation', 'scholarship_holder', 'active', 'entry_date', 'departure_date')


class PositionForm(forms.ModelForm):
	class Meta:
		model = Position
		fields = ('name', 'description')


class InstituitionForm(forms.ModelForm):
	class Meta:
		model = Instituition
		fields = ('name', 'description')


class ActuationForm(forms.ModelForm):
	class Meta:
		model = Actuation
		fields = ('name', 'description')


class SpecialtyForm(forms.ModelForm):
	class Meta:
		model = Specialty
		fields = ('name', 'description')