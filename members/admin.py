from django.contrib import admin
from .models import Member, Instituition, Position, Actuation, Specialty


admin.site.register(Member)
admin.site.register(Instituition)
admin.site.register(Position)
admin.site.register(Actuation)
admin.site.register(Specialty)