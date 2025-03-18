from django.contrib import admin
from .models import Employee,role,department

# Register your models here.
admin.site.register(Employee)
admin.site.register(role)
admin.site.register(department)
