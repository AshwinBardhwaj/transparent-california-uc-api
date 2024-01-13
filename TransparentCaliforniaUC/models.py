from django.db import models
from djmoney.models.fields import MoneyField

class UCEmployee(models.Model):
    Benefits = models.DecimalField(max_digits=10, decimal_places=2)#MoneyField(max_digits=12, decimal_places=2, default_currency='USD')
    ID = models.IntegerField(primary_key=True)
    Job_Title = models.CharField(max_length = 300)
    Name = models.CharField(max_length=200)
    Other_Pay = models.DecimalField(max_digits=10, decimal_places=2)#MoneyField(max_digits=12, decimal_places=2, default_currency='USD')
    Overtime_Pay = models.DecimalField(max_digits=10, decimal_places=2)#MoneyField(max_digits=10, decimal_places=2, default_currency='USD')
    Regular_Pay = models.DecimalField(max_digits=10, decimal_places=2)#MoneyField(max_digits=12, decimal_places=2, default_currency='USD')
    Total_Pay = models.DecimalField(max_digits=10, decimal_places=2)#MoneyField(max_digits=12, decimal_places=2, default_currency='USD')
    Total_Pay_And_Benefits = models.DecimalField(max_digits=10, decimal_places=2)#MoneyField(max_digits=12, decimal_places=2, default_currency='USD')
    
    def __str__(self):
        return self.Name
    
    class Meta:
        ordering = ["ID"]