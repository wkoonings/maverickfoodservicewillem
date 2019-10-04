from django.contrib import admin

from .models import Customer, Service, Product, Profile

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'date_of_birth', 'photo']

class CustomerList(admin.ModelAdmin):
    list_display = ( 'cust_name', 'organization', 'phone_number')
    list_filter = ( 'cust_name', 'organization')
    search_fields = ('cust_name', )
    ordering = ['cust_name']

class ServiceList(admin.ModelAdmin):
    list_display = ('cust_name', 'service_category', 'setup_time')
    list_filter = ('cust_name', 'setup_time')
    search_fields = ('cust_name',)
    ordering = ['cust_name']

class ProductList(admin.ModelAdmin):
    list_display = ('cust_name', 'product', 'pickup_time')
    list_filter = ('cust_name', 'pickup_time')
    search_fields = ('cust_name',)
    ordering = ['cust_name']

admin.site.register(Customer, CustomerList)
admin.site.register(Service, ServiceList)
admin.site.register(Product, ProductList)

