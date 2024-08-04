from django.db import models

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
    full_quantity = models.DecimalField(max_digits=10, decimal_places=2)  
    leaves_quantity = models.DecimalField(max_digits=10, decimal_places=2)  
    gold_leaves = models.DecimalField(max_digits=10, decimal_places=2)  # Adjust as needed
    empty_cases = models.IntegerField()  # Assuming empty_cases is an integer
    water = models.DecimalField(max_digits=10, decimal_places=2)  # Adjust as needed
    matured_leaves = models.DecimalField(max_digits=10, decimal_places=2)  # Adjust as needed
    boiled_leaves = models.DecimalField(max_digits=10, decimal_places=2)  # Adjust as needed
    good_leaves = models.DecimalField(max_digits=10, decimal_places=2)  
    supervision = models.ForeignKey('Supervision', on_delete=models.CASCADE)  
    officer = models.ForeignKey('Officer', on_delete=models.CASCADE)  
    contact_info = models.CharField(max_length=255)
    address = models.TextField()
    bank = models.ForeignKey(Bank, on_delete=models.CASCADE)

    def __str__(self):
        return self.supplier_name

class Officer(models.Model):
    Officer_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)


    def __str__(self):
        return self.name

class Supervision(models.Model):
    supervision_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)


    def __str__(self):
        return self.name

class Root(models.Model):
    root_id = models.AutoField(primary_key=True)
    root_name = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.root_name


class Transaction(models.Model):
    transaction_id = models.AutoField(primary_key=True)
    customer_id = models.IntegerField()
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE)
    root = models.ForeignKey(Root, on_delete=models.CASCADE)
    transaction_date = models.DateTimeField()
    quantity = models.IntegerField()
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f'Transaction {self.transaction_id}'
