from django.shortcuts import render, get_object_or_404 # can be used when working with VIEWSET
# from django.http import JsonResponse
from rest_framework import status, mixins, generics, viewsets
from students.models import Student
from .serializers import StudentSerializer, EmployeeSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from employee.models import Employee
from django.http import Http404
from blog.models import *
from blog.serializers import *
from .paginations import CustomPagination
from django_filters.rest_framework import DjangoFilterBackend
from employee.filters import EmployeeFilter


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

@api_view(['GET', 'PUT', 'DELETE'])
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
            return Response(serializer.data , status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)
        
    elif request.method == 'DELETE':
        student.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

        
'''
# USING CLASS BASED IS TOO EASY!
class Employees(APIView):
    def get(self, request):
        employee = Employee.objects.all()
        serielizer = EmployeeSerializer(employee, many=True)
        return Response(serielizer.data, status=status.HTTP_200_OK)
    
    def post(self, request):
        serializer = EmployeeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)
    

class EmployeeDetails(APIView):
    def get_object(self, pk):
        try:
            return Employee.objects.get(pk=pk)
        except Employee.DoesNotExist:
            raise Http404
            
    def get(self, request, pk):
        employee = self.get_object(pk)
        serializer = EmployeeSerializer(employee)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def put(self, request, pk):
        employee = self.get_object(pk)
        serializer = EmployeeSerializer(employee, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

    def delete(self, request, pk):
        employee = self.get_object(pk)
        employee.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
'''

'''
# USING MIXIN IS MUCH EASIER THAN ALL THE ABOVE.
class Employees(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

    def get(self, request):
        return self.list(request)
    
    def post(self, request):
        return self.create(request)
    
class EmployeeDetails(mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin, generics.GenericAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

    def get(self, request, pk):
        return self.retrieve(request, pk) 
    
    def put(self, request, pk):
        return self.update(request, pk)
    
    def delete(self, request, pk):
        return self.destroy(request, pk)
'''

# THERE IS ANOTHER FUTHER PATH FOR CRETING APIs! GENERICS
# FIRST METHOD USING ONLY ListAPIView METHOD TO GET THE USERS INFO;

# class Employees(generics.ListAPIView):
#     queryset = Employee.objects.all()
#     serializer_class = EmployeeSerializer

# SECOND METHOD USING ONLY list & create METHOD TO GET & POSt THE USERS INFO;
# class Employees(generics.ListAPIView, generics.CreateAPIView):
#     queryset = Employee.objects.all()
#     serializer_class = EmployeeSerializer

# THIRD METHOD USING ONLY listCreateAPIView METHOD TO GET & POST THE USERS INFO;
# class Employees(generics.ListCreateAPIView):
#     queryset = Employee.objects.all()
#     serializer_class = EmployeeSerializer

# TO UPDATE | DELETE USER INFO WE USED generic.UpdateAPIView, generics.DestroyAPIView as parameter
# class EmployeeDetails(generics.RetrieveAPIView, generics.UpdateAPIView, generics.DestroyAPIView):
    # queryset = Employee.objects.all()
    # serializer_class = EmployeeSerializer
    # TO GET SPECIFIC USER INFO WE USED lookup_field = 'pk'
    # lookup_field = 'pk'

# SHORCUT WAY GET | UPDATE | DESTROY USER DATA:
# class EmployeeDetails(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Employee.objects.all()
#     serializer_class = EmployeeSerializer
#     lookup_field = 'pk'

'''
# USING VIESET
class EmployeeViewSet(viewsets.ViewSet):
    def list(self, request):
        queryset = Employee.objects.all()
        serializer = EmployeeSerializer(queryset, many=True)
        return Response(serializer.data) # Ko ba status Code Yana aiki
    
    def create(self, request): # OR post() will work Ok
        serializer = EmployeeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors)
    
    def retrieve(self, request, pk=None):
        employee = get_object_or_404(Employee, pk=pk)
        serializer = EmployeeSerializer(employee)
        return Response(serializer.data)
    
    def update(self, request, pk=None):
        employee = get_object_or_404(Employee, pk=pk)
        serializer = EmployeeSerializer(employee, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    
'''

# USING JUST VIEWMODELSET WILL CREATE A COMPLETE CRUD OPs. SIMPLE AS ABCD hUH!
class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all().order_by('pk')
    serializer_class = EmployeeSerializer
    pagination_class = CustomPagination
    # filterset_fields = ['designation'] # Wanna filter bata search na case sensitive! kuma nayi ma bai ba!
    filter_backends = [DjangoFilterBackend]
    filterset_class = EmployeeFilter

class BlogViews(generics.ListCreateAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer

class CommentViews(generics.ListCreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

class BlogDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    lookup_field = 'pk'


class CommentsDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    lookup_field = 'pk'