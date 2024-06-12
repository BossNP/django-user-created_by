from django.shortcuts import render

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .models import Customer, Gender
from .serializers import CustomerSerializer, GenderSerializer

@api_view(['POST','GET', 'PUT', 'DELETE'])
def CustomerAPI(request, pk:int = None):
    if request.method == 'GET':
        if pk is None:
            # Retrieve all rows
            customers = Customer.objects.all()
            serializer = CustomerSerializer(customers, many=True)
            return Response(serializer.data)
        else:
            # Retrieve a specific row by ID
            try:
                customer = Customer.objects.get(customer_id=pk)
            except Customer.DoesNotExist:
                return Response(status=status.HTTP_404_NOT_FOUND)
            serializer = CustomerSerializer(customer)
            return Response(serializer.data)
    
    elif request.method == 'POST':
        serializer = CustomerSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save(created_by=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'PUT':
        try:
            customer = Customer.objects.get(customer_id=pk)
        except Customer.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = CustomerSerializer(customer, data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save(updated_by=request.user)
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        try:
            customer = Customer.objects.get(customer_id=pk)
        except Customer.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        customer.delete()
        return Response({'A Customer deleted successfully.'}, status=status.HTTP_204_NO_CONTENT)


@api_view(['POST','GET', 'PUT', 'DELETE'])
# @permission_classes([IsAuthenticated])
def GenderAPI(request, pk:int = None):
    # if not request.user.is_authenticated:
    #     return Response({'detail': 'Authentication credentials were not provided.'}, status=status.HTTP_401_UNAUTHORIZED)

    if request.method == 'GET':
        if pk is None:
            # Retrieve all rows
            genders = Gender.objects.all()
            serializer = GenderSerializer(genders, many=True)
            return Response(serializer.data)
        else:
            # Retrieve a specific row by ID
            try:
                gender = Gender.objects.get(gender_id=pk)
            except Gender.DoesNotExist:
                return Response(status=status.HTTP_404_NOT_FOUND)
            serializer = GenderSerializer(gender)
            return Response(serializer.data)
    
    elif request.method == 'POST':
        serializer = GenderSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save(created_by=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'PUT':
        try:
            gender = Gender.objects.get(gender_id=pk)
        except Gender.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = GenderSerializer(gender, data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save(updated_by=request.user)
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        try:
            gender = Gender.objects.get(gender_id=pk)
        except Gender.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        gender.delete()
        return Response({'A Gender deleted successfully.'}, status=status.HTTP_204_NO_CONTENT)