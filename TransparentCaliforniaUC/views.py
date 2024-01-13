from django.http import JsonResponse
from .models import UCEmployee
from .serializers import UCEmployeeSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view

def employee_list(request):
    employees = UCEmployee.objects.all()
    serializer = UCEmployeeSerializer(employees, many=True)
    return JsonResponse({"UCEmployees": serializer.data}, safe=False)

@api_view(['GET'])
def employee_individual(request, id):
    try:
        employee = UCEmployee.objects.get(pk=id)
    except UCEmployee.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    serializer = UCEmployeeSerializer(employee)
    return Response(serializer.data)
    