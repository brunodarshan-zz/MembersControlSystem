# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from django.db import models
from django.core.validators import MinLengthValidator

class Member(models.Model):
	name = models.CharField(max_length=200, null=False, verbose_name='Nome')
	cpf = models.CharField(max_length=14, validators=[MinLengthValidator(11)], null=False, verbose_name='CPF')
	rg = models.CharField(max_length=20, null=False, verbose_name='RG')
	position = models.ForeignKey('Position', null=False, verbose_name='Cargo')
	instituition = models.ForeignKey('Instituition', null=False, verbose_name='Instituição')
	actuations = models.ManyToManyField('Actuation', verbose_name='Atuações', help_text='Mantenha pressionado o Control (CTRL), ou Command no Mac, para selecionar mais de uma opção.')
	contact = models.CharField(max_length=11, null=False, verbose_name='Contato')
	specialties = models.ManyToManyField('Specialty', verbose_name='Especialidades', help_text='Mantenha pressionado o Control (CTRL), ou Command no Mac, para selecionar mais de uma opção.')
	student_ifpi = models.BooleanField(default=False, verbose_name='Aluno do IFPI')
	matriculation = models.CharField(max_length=12, blank=True, null=True, verbose_name='Matrícula', help_text='Se não for aluno do IFPI, deixe em branco.')
	scholarship_holder = models.BooleanField(default=False, verbose_name='Bolsista')
	active = models.BooleanField(default=False, verbose_name='Ativo')
	entry_date = models.DateField(blank=True, null=True, verbose_name='Data de Entrada')
	departure_date = models.DateField(blank=True, null=True, verbose_name='Data de Saída')


	def register(self):
		self.save()


	def __str__(self):
		return self.name


class Position(models.Model):
	name = models.CharField(max_length=200, null=False, verbose_name='Nome')
	description = models.TextField(verbose_name='Descrição')


	def register(self):
		self.save()


	def __str__(self):
		return self.name


class Instituition(models.Model):
	name = models.CharField(max_length=200, null=False, verbose_name='Nome')
	description = models.TextField(verbose_name='Descrição')


	def register(self):
		self.save()


	def __str__(self):
		return self.name


class Actuation(models.Model):
	name = models.CharField(max_length=200, null=False, verbose_name='Nome')
	description = models.TextField(verbose_name='Descrição')


	def register(self):
		self.save()


	def __str__(self):
		return self.name


class Specialty(models.Model):
	name = models.CharField(max_length=200, null=False, verbose_name='Nome')
	description = models.TextField(verbose_name='Descrição')


	def register(self):
		self.save()


	def __str__(self):
		return self.name