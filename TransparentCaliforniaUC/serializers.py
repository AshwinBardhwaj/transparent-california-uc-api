from rest_framework import serializers
from .models import UCEmployee

class UCEmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = UCEmployee
        fields = ['ID', 'Name', 'Job_Title', 'Regular_Pay', 'Overtime_Pay', 'Other_Pay', 'Total_Pay', 'Benefits', 'Total_Pay_And_Benefits']