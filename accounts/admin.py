from django.contrib import admin
from .models import EmployeeAccount,CustomerAccount,User
from django.contrib.auth.models import Group

admin.site.register(User)
admin.site.unregister(Group)
admin.site.register(EmployeeAccount)
admin.site.register(CustomerAccount)