from django.contrib import admin
from .models import Bank, Supplier, Officer, Supervision, Root, Transaction

class BankAdmin(admin.ModelAdmin):
    list_display = ('bank_id', 'bank_name', 'bank_branch', 'account_number')
    search_fields = ('bank_name', 'bank_branch')

class SupplierAdmin(admin.ModelAdmin):
    list_display = ('supplier_id', 'supplier_name', 'record_id', 'date', 'contact_info', 'bank')
    search_fields = ('supplier_name', 'record_id', 'contact_info')
    list_filter = ('date', 'bank')

class OfficerAdmin(admin.ModelAdmin):
    list_display = ('Officer_id', 'name')
    search_fields = ('name',)

class SupervisionAdmin(admin.ModelAdmin):
    list_display = ('supervision_id', 'name')
    search_fields = ('name',)

class RootAdmin(admin.ModelAdmin):
    list_display = ('root_id', 'root_name', 'description')
    search_fields = ('root_name',)

class TransactionAdmin(admin.ModelAdmin):
    list_display = ('transaction_id', 'customer_id', 'supplier', 'root', 'transaction_date', 'quantity', 'total_amount')
    search_fields = ('customer_id', 'supplier__supplier_name', 'root__root_name')
    list_filter = ('transaction_date', 'supplier', 'root')

admin.site.register(Bank, BankAdmin)
admin.site.register(Supplier, SupplierAdmin)
admin.site.register(Officer, OfficerAdmin)
admin.site.register(Supervision, SupervisionAdmin)
admin.site.register(Root, RootAdmin)
admin.site.register(Transaction, TransactionAdmin)
