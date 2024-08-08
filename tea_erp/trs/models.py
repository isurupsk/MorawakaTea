

from django.db import models


# Users  tables 

class UserRole(models.Model):
    user_role_id = models.AutoField(primary_key=True)
    user_role = models.CharField(max_length=255)
    status = models.BooleanField(default=True)

    def __str__(self):
        return self.user_role
    
class User(models.Model):
    user_id = models.AutoField(primary_key=True)
    user_name = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    status = models.BooleanField(default=True)
    created_date = models.DateTimeField(auto_now_add=True)
    user_role = models.ForeignKey(UserRole, on_delete=models.CASCADE)

    def __str__(self):
        return self.user_name


class Bank(models.Model):
    bank_id = models.AutoField(primary_key=True)
    bank_name = models.CharField(max_length=255)
    bank_branch = models.CharField(max_length=255)
    account_number = models.CharField(max_length=50)

    def __str__(self):
        return self.bank_name

class Supplier(models.Model):
    supplier_id = models.AutoField(primary_key=True)
    record_id = models.CharField(max_length=255)  
    supplier_name = models.CharField(max_length=255)
    date = models.DateField() 
    contact_info = models.CharField(max_length=255)
    address = models.TextField()
    land_size = models.DecimalField(max_digits=10, decimal_places=2) 
    bank = models.ForeignKey(Bank, on_delete=models.CASCADE)

    def __str__(self):
        return self.supplier_name

class Root(models.Model):
    root_id = models.AutoField(primary_key=True)
    root_name = models.CharField(max_length=255)
    root_code = models.CharField(max_length=50)
    description = models.TextField()

    def __str__(self):
        return self.root_name

class Officer(models.Model):
    officer_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Supervision(models.Model):
    supervision_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    
class RootTransportAgent(models.Model):
    root_transport_agent_id = models.AutoField(primary_key=True)

    agent_name = models.CharField(max_length=255)

    def __str__(self):
        return f'Transport Agent {self.agent_name}'

class DailyGreenLeaf(models.Model):
    daily_green_leaf_id = models.AutoField(primary_key=True)
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE)
    root = models.ForeignKey(Root, on_delete=models.CASCADE)
    date = models.DateField() 
    full_quantity = models.DecimalField(max_digits=10, decimal_places=2)
    leaves_quantity = models.DecimalField(max_digits=10, decimal_places=2)
    gold_leaves = models.DecimalField(max_digits=10, decimal_places=2)
    empty_cases = models.IntegerField()
    water = models.DecimalField(max_digits=10, decimal_places=2)
    matured_leaves = models.DecimalField(max_digits=10, decimal_places=2)
    boiled_leaves = models.DecimalField(max_digits=10, decimal_places=2)
    good_leaves = models.DecimalField(max_digits=10, decimal_places=2)
    supervision = models.ForeignKey(Supervision, on_delete=models.CASCADE)
    officer = models.ForeignKey(Officer, on_delete=models.CASCADE)
    root_transport_agent = models.ForeignKey(RootTransportAgent, on_delete=models.CASCADE)

    def __str__(self):
        return f'Daily Green Leaf {self.daily_green_leaf_id}'

class SupplierPayment(models.Model):
    supplier_payment_id = models.AutoField(primary_key=True)
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE)
    root = models.ForeignKey(Root, on_delete=models.CASCADE)
    transaction_date = models.DateTimeField()
    quantity = models.IntegerField()
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f'Transaction {self.supplier_payment_id}'

# New Models
class Loan(models.Model):
    loan_id = models.AutoField(primary_key=True)
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE)
    date = models.DateField()
    loan_amount = models.DecimalField(max_digits=10, decimal_places=2)
    root = models.ForeignKey(Root, on_delete=models.CASCADE)

    def __str__(self):
        return f'Loan {self.loan_id}'

class AdvancePayment(models.Model):
    advance_payment_id = models.AutoField(primary_key=True)
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE)
    date = models.DateField()
    advance_amount = models.DecimalField(max_digits=10, decimal_places=2)
    root = models.ForeignKey(Root, on_delete=models.CASCADE)

    def __str__(self):
        return f'Advance Payment {self.advance_payment_id}'





class RootTransport(models.Model):
    root_transport_id = models.AutoField(primary_key=True)
    root = models.ForeignKey(Root, on_delete=models.CASCADE)
    transport_agent = models.ForeignKey(RootTransportAgent, on_delete=models.CASCADE)

    def __str__(self):
        return f'Root Transport {self.root_transport_id}'

class PaymentMode(models.Model):
    payment_mode_id = models.AutoField(primary_key=True)
    payment_mode = models.CharField(max_length=255)

    def __str__(self):
        return self.payment_mode

class SupplierPayment(models.Model):
    supplier_payment_id = models.AutoField(primary_key=True)
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE)
    payment_mode = models.ForeignKey(PaymentMode, on_delete=models.CASCADE)
    transaction_date = models.DateTimeField()
    quantity = models.IntegerField()
    cheque_number = models.CharField(max_length=50, null=True, blank=True)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f'Transaction {self.supplier_payment_id}'
    
class Loan(models.Model):
    loan_id = models.AutoField(primary_key=True)
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE)
    date = models.DateField()
    loan_amount = models.DecimalField(max_digits=10, decimal_places=2)
    root = models.ForeignKey(Root, on_delete=models.CASCADE)
    cheque_number = models.CharField(max_length=50, null=True, blank=True)
    payment_mode = models.ForeignKey(PaymentMode, on_delete=models.CASCADE)

    def __str__(self):
        return f'Loan {self.loan_id}'

class AdvancePayment(models.Model):
    advance_payment_id = models.AutoField(primary_key=True)
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE)
    date = models.DateField()
    advance_amount = models.DecimalField(max_digits=10, decimal_places=2)
    root = models.ForeignKey(Root, on_delete=models.CASCADE)
    cheque_number = models.CharField(max_length=50, null=True, blank=True)
    payment_mode = models.ForeignKey(PaymentMode, on_delete=models.CASCADE)

    def __str__(self):
        return f'Advance Payment {self.advance_payment_id}'
    
class LoanRepayment(models.Model):
    loan_repayment_id = models.AutoField(primary_key=True)
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE)
    date = models.DateField()
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    root = models.ForeignKey(Root, on_delete=models.CASCADE)
    loan = models.ForeignKey(Loan, on_delete=models.CASCADE)
    balance = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f'Loan Repayment {self.loan_repayment_id}'


