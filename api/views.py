# from django.shortcuts import render
# from django.http import JsonResponse
from rest_framework import status
from students.models import Student
from .serializers import StudentSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view

@api_view(['GET', 'POST'])
def studentsView(request):
    if request.method == 'GET':
        students = Student.objects.all()
        serializer = StudentSerializer(students, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    elif request.method == 'POST':
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    # MANUAL WAY OF SENDING DATA THROUGH API
    # students = {
    #     'id': 1,
    #     'full_name': 'Mukhtar Bello Sarki',
    #     'email': 'mukhatar@semail.com',
    #     'username': 'mukhtarSarki10',
    #     'password': 'PF48JDANCJFH94Q;SAJAD841JHEUQIEQ',
    #     'address': 'N0.29 Garki Road, Abuja FCT Nigeria'

    # }

    # This also is not recommended Way of creating Api cux it's Manual way!
    # students = Student.objects.all()
    # student_data = list(students.values()) 

    # return JsonResponse(student_data, safe=False)

    # USING RECOMMENDED WAY

@api_view(['GET'])
def studentDetailsView(request, pk):
    try:
        student = Student.objects.get(pk=pk)
    except Student.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = StudentSerializer(student)
        return Response(serializer.data, status=status.HTTP_200_OK)

    elif request.method == 'PUT':
        serializer = StudentSerializer(student, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.errors, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)