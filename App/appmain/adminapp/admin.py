# from django.contrib import admin
from django.contrib.admin import AdminSite
from usersapp.models import Location, Type_of_activity, Company, Menu, Table_of_restaurant, Services_of_institutions, Order, Review
from django.contrib.auth.models import Group, User

# Register your models here.
class MyAdminSite(AdminSite):
    site_header = 'Yopup admin panel'


New_models = [Location, Type_of_activity, Company, Menu, Table_of_restaurant, Services_of_institutions, Order, Review, Group, User]
admin_site = MyAdminSite(name='myadmin')
admin_site.register(New_models)