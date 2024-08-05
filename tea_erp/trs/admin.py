from django.contrib import admin
from .models import (
    Bank, Supplier, Root, Officer, Supervision,
    DailyGreenLeaf, SupplierPayment, Loan,
    AdvancePayment, LoanRepayment, RootTransportAgent, RootTransport
)

class BankAdmin(admin.ModelAdmin):
    list_display = ('bank_id', 'bank_name', 'bank_branch', 'account_number')

class SupplierAdmin(admin.ModelAdmin):
    list_display = ('supplier_id', 'record_id', 'supplier_name', 'date', 'contact_info', 'address', 'bank')

class RootAdmin(admin.ModelAdmin):
    list_display = ('root_id', 'root_name', 'description')

class OfficerAdmin(admin.ModelAdmin):
    list_display = ('officer_id', 'name')

class SupervisionAdmin(admin.ModelAdmin):
    list_display = ('supervision_id', 'name')

class DailyGreenLeafAdmin(admin.ModelAdmin):
    list_display = ('daily_green_leaf_id', 'supplier', 'root', 'date', 'full_quantity', 'leaves_quantity', 
                    'gold_leaves', 'empty_cases', 'water', 'matured_leaves', 'boiled_leaves', 
                    'good_leaves', 'supervision', 'officer')

class SupplierPaymentAdmin(admin.ModelAdmin):
    list_display = ('supplier_payment_id', 'supplier', 'root', 'transaction_date', 'quantity', 'total_amount')

class LoanAdmin(admin.ModelAdmin):
    list_display = ('loan_id', 'supplier', 'date', 'loan_amount', 'root')

class AdvancePaymentAdmin(admin.ModelAdmin):
    list_display = ('advance_payment_id', 'supplier', 'date', 'advance_amount', 'root')

class LoanRepaymentAdmin(admin.ModelAdmin):
    list_display = ('loan_repayment_id', 'supplier', 'date', 'amount', 'root', 'loan', 'balance')

class RootTransportAgentAdmin(admin.ModelAdmin):
    list_display = ('root_transport_agent_id', 'supplier', 'agent_name')

class RootTransportAdmin(admin.ModelAdmin):
    list_display = ('root_transport_id', 'root', 'transport_agent')

admin.site.register(Bank, BankAdmin)
admin.site.register(Supplier, SupplierAdmin)
admin.site.register(Root, RootAdmin)
admin.site.register(Officer, OfficerAdmin)
admin.site.register(Supervision, SupervisionAdmin)
admin.site.register(DailyGreenLeaf, DailyGreenLeafAdmin)
admin.site.register(SupplierPayment, SupplierPaymentAdmin)
admin.site.register(Loan, LoanAdmin)
admin.site.register(AdvancePayment, AdvancePaymentAdmin)
admin.site.register(LoanRepayment, LoanRepaymentAdmin)
admin.site.register(RootTransportAgent, RootTransportAgentAdmin)
admin.site.register(RootTransport, RootTransportAdmin)
