# from django.contrib import admin
# from .models import (
#     Bank, Supplier, Root, Officer, Supervision,
#     DailyGreenLeaf, SupplierPayment, Loan,
#     AdvancePayment, LoanRepayment, RootTransportAgent, RootTransport
# )

# class BankAdmin(admin.ModelAdmin):
#     list_display = ('bank_id', 'bank_name', 'bank_branch', 'account_number')

# class SupplierAdmin(admin.ModelAdmin):
#     list_display = ('supplier_id', 'record_id', 'supplier_name', 'date', 'contact_info', 'address', 'bank')

# class RootAdmin(admin.ModelAdmin):
#     list_display = ('root_id', 'root_name', 'description')

# class OfficerAdmin(admin.ModelAdmin):
#     list_display = ('officer_id', 'name')

# class SupervisionAdmin(admin.ModelAdmin):
#     list_display = ('supervision_id', 'name')

# class DailyGreenLeafAdmin(admin.ModelAdmin):
#     list_display = ('daily_green_leaf_id', 'supplier', 'root', 'date', 'full_quantity', 'leaves_quantity', 
#                     'gold_leaves', 'empty_cases', 'water', 'matured_leaves', 'boiled_leaves', 
#                     'good_leaves', 'supervision', 'officer')

# class SupplierPaymentAdmin(admin.ModelAdmin):
#     list_display = ('supplier_payment_id', 'supplier', 'root', 'transaction_date', 'quantity', 'total_amount')

# class LoanAdmin(admin.ModelAdmin):
#     list_display = ('loan_id', 'supplier', 'date', 'loan_amount', 'root')

# class AdvancePaymentAdmin(admin.ModelAdmin):
#     list_display = ('advance_payment_id', 'supplier', 'date', 'advance_amount', 'root')

# class LoanRepaymentAdmin(admin.ModelAdmin):
#     list_display = ('loan_repayment_id', 'supplier', 'date', 'amount', 'root', 'loan', 'balance')

# class RootTransportAgentAdmin(admin.ModelAdmin):
#     list_display = ('root_transport_agent_id', 'supplier', 'agent_name')

# class RootTransportAdmin(admin.ModelAdmin):
#     list_display = ('root_transport_id', 'root', 'transport_agent')

# admin.site.register(Bank, BankAdmin)
# admin.site.register(Supplier, SupplierAdmin)
# admin.site.register(Root, RootAdmin)
# admin.site.register(Officer, OfficerAdmin)
# admin.site.register(Supervision, SupervisionAdmin)
# admin.site.register(DailyGreenLeaf, DailyGreenLeafAdmin)
# admin.site.register(SupplierPayment, SupplierPaymentAdmin)
# admin.site.register(Loan, LoanAdmin)
# admin.site.register(AdvancePayment, AdvancePaymentAdmin)
# admin.site.register(LoanRepayment, LoanRepaymentAdmin)
# admin.site.register(RootTransportAgent, RootTransportAgentAdmin)
# admin.site.register(RootTransport, RootTransportAdmin)




from django.contrib import admin
from .models import (
    UserRole, User, Bank, Supplier, Root, Officer, Supervision, 
    RootTransportAgent, DailyGreenLeaf, SupplierPayment, Loan, 
    AdvancePayment, LoanRepayment, RootTransport, PaymentMode
)

@admin.register(UserRole)
class UserRoleAdmin(admin.ModelAdmin):
    list_display = ('user_role_id', 'user_role', 'status')
    search_fields = ('user_role',)
    list_filter = ('status',)

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('user_id', 'user_name', 'status', 'created_date', 'user_role')
    search_fields = ('user_name',)
    list_filter = ('status', 'user_role')

@admin.register(Bank)
class BankAdmin(admin.ModelAdmin):
    list_display = ('bank_id', 'bank_name', 'bank_branch', 'account_number')
    search_fields = ('bank_name', 'bank_branch')

@admin.register(Supplier)
class SupplierAdmin(admin.ModelAdmin):
    list_display = ('supplier_id', 'supplier_name', 'contact_info', 'address', 'land_size', 'bank')
    search_fields = ('supplier_name', 'contact_info', 'record_id')
    list_filter = ('bank',)

@admin.register(Root)
class RootAdmin(admin.ModelAdmin):
    list_display = ('root_id', 'root_name', 'root_code', 'description')
    search_fields = ('root_name', 'root_code')

@admin.register(Officer)
class OfficerAdmin(admin.ModelAdmin):
    list_display = ('officer_id', 'name', 'user')
    search_fields = ('name',)
    list_filter = ('user',)

@admin.register(Supervision)
class SupervisionAdmin(admin.ModelAdmin):
    list_display = ('supervision_id', 'name', 'user')
    search_fields = ('name',)
    list_filter = ('user',)

@admin.register(RootTransportAgent)
class RootTransportAgentAdmin(admin.ModelAdmin):
    list_display = ('root_transport_agent_id', 'agent_name')
    search_fields = ('agent_name',)

@admin.register(DailyGreenLeaf)
class DailyGreenLeafAdmin(admin.ModelAdmin):
    list_display = ('daily_green_leaf_id', 'supplier', 'root', 'date', 'full_quantity', 'leaves_quantity')
    search_fields = ('supplier__supplier_name', 'root__root_name')
    list_filter = ('supplier', 'root', 'date')

@admin.register(SupplierPayment)
class SupplierPaymentAdmin(admin.ModelAdmin):
    list_display = ('supplier_payment_id', 'supplier', 'payment_mode', 'transaction_date', 'total_amount', 'cheque_number')
    search_fields = ('supplier__supplier_name', 'cheque_number')
    list_filter = ('supplier', 'payment_mode', 'transaction_date')

@admin.register(Loan)
class LoanAdmin(admin.ModelAdmin):
    list_display = ('loan_id', 'supplier', 'date', 'loan_amount', 'root', 'cheque_number', 'payment_mode')
    search_fields = ('supplier__supplier_name', 'cheque_number')
    list_filter = ('supplier', 'root', 'payment_mode', 'date')

@admin.register(AdvancePayment)
class AdvancePaymentAdmin(admin.ModelAdmin):
    list_display = ('advance_payment_id', 'supplier', 'date', 'advance_amount', 'root', 'cheque_number', 'payment_mode')
    search_fields = ('supplier__supplier_name', 'cheque_number')
    list_filter = ('supplier', 'root', 'payment_mode', 'date')

@admin.register(LoanRepayment)
class LoanRepaymentAdmin(admin.ModelAdmin):
    list_display = ('loan_repayment_id', 'supplier', 'date', 'amount', 'balance', 'loan', 'root')
    search_fields = ('supplier__supplier_name',)
    list_filter = ('supplier', 'root', 'date')

@admin.register(RootTransport)
class RootTransportAdmin(admin.ModelAdmin):
    list_display = ('root_transport_id', 'root', 'transport_agent')
    search_fields = ('root__root_name', 'transport_agent__agent_name')
    list_filter = ('root', 'transport_agent')

@admin.register(PaymentMode)
class PaymentModeAdmin(admin.ModelAdmin):
    list_display = ('payment_mode_id', 'payment_mode')
    search_fields = ('payment_mode',)
