# views.py
from django.shortcuts import render
from .models import Task,User
from rest_framework import viewsets
from .serializers import TaskSerializer
from .forms import TaskForm
from rest_framework.response import Response
from rest_framework import status
import logging
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from rest_framework.decorators import api_view,permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView
from rest_framework import permissions
from django.contrib.auth import authenticate
from .utils import *



def task_list(request):
    """
    FUNCTION FOR DISPLAY ALL TASK DETAILS
    """
    tasks = Task.objects.all()
    return render(request, 'tasks/task_list.html', {'tasks': tasks})


def home(request):
    """
    FUNCTION FOR RETURN USER TO HOME
    """
    return render(request, 'tasks/home.html', {'tasks': None})



class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer



def add_task(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            # Redirect or perform other actions upon successful form submission
    else:
        form = TaskForm()

    return render(request, 'tasks/add_task.html', {'form': form})


@api_view(['POST'])
@permission_classes([AllowAny])
@csrf_exempt
def sum_of_even_numbers(request):
    """
    Calculate the sum of all even numbers in the given list.

    Parameters:
    - numbers (list): List of numbers.

    Returns:
    - int: Sum of even numbers.
    """
    try:
        numbers = request.data['numbers']
        VALUE =  sum(num for num in numbers if num % 2 == 0)
        res = {'status':True,'message':"Success",'data':VALUE}
        return JsonResponse(res,status=status.HTTP_200_OK,safe=False)
    
    except Exception as e:
        logging.info(e)
        res = {'status':False,'message':"Server Error",'data':[]}
        return JsonResponse(res,status=status.HTTP_400_BAD_REQUEST)
    
    
    
class ManageTask(APIView):
    permission_classes = [permissions.IsAuthenticated]
    
    def get(self,request):
        #LIST ALL TASK DETAILS FOR PARTICULAR USER
        try:
            task_data = Task.objects.filter(created_by_id=request.user.id).values().order_by('-id')
            res = {'status':True,'message':'Task Listed Successfully','data':task_data}
            return Response(res,status=status.HTTP_200_OK)
        
        except Exception as e:
            logging.info(e)
            res = {'status':False,'message':"Server Error",'data':[]}
            return JsonResponse(res,status=status.HTTP_400_BAD_REQUEST)
        
    def post(self,request):
        #API FOR CREATE A NEW TASKS
        try:
            data = request.data
            
            #VALIDATIONS OF KEYS
            
            required_keys = ["title","description","dueDate","completed"]
            
            for keys in required_keys:
                if keys not in data:
                    res = {'status':False,'message':f"Please provide {keys}",'data':[]}
                    return JsonResponse(res,status=status.HTTP_400_BAD_REQUEST)
                if keys == None or len(keys)<=0:
                    res = {'status':False,'message':f"Please choose value for {keys}",'data':[]}
                    return JsonResponse(res,status=status.HTTP_400_BAD_REQUEST)
                
                
            #SAVE NEW TASK
            data['created_by'] = request.user.id
            task_data = TaskSerializer(data=data)
            if task_data.is_valid():
                task_data.save()
                
                res = {'status':True,'message':'Task created successfully','data':[]}
                return Response(res,status=status.HTTP_200_OK)
            
            else:
                res = {'status':False,'message':"Please check the details",'data':[]}
                return Response(res,status=status.HTTP_400_BAD_REQUEST)
                    
            
        except Exception as e:
            logging.info(e)
            res = {'status':False,'message':"Server Error",'data':[]}
            return JsonResponse(res,status=status.HTTP_400_BAD_REQUEST)
        
    def put(self,request):
        #API FOR UPDATE THE EXISTING TASK
        try:
            data = request.data
            
            #VALIDATIONS OF KEYS
            
            required_keys = ["title","description","dueDate","completed"]
            
            for keys in required_keys:
                if keys not in data:
                    res = {'status':False,'message':f"Please provide {keys}",'data':[]}
                    return JsonResponse(res,status=status.HTTP_400_BAD_REQUEST)
                if keys == None or len(keys)<=0:
                    res = {'status':False,'message':f"Please choose value for {keys}",'data':[]}
                    return JsonResponse(res,status=status.HTTP_400_BAD_REQUEST)
                                
            #SAVE NEW TASK
            task_obj = Task.objects.filter(id=data['id'],created_by_id=request.user.id).last()
            
            if task_obj == None:
                res = {'status':False,'message':'Task not found','data':[]}
                return Response(res,status=status.HTTP_400_BAD_REQUEST)
            
            task_data = TaskSerializer(task_obj,data=data)
            if task_data.is_valid():
                task_data.save()                
                res = {'status':True,'message':'Task updated successfully','data':[]}
                return Response(res,status=status.HTTP_200_OK)
            
            else:
                res = {'status':False,'message':"Please check the details",'data':[]}
                return Response(res,status=status.HTTP_400_BAD_REQUEST)
                    
            
        except Exception as e:
            logging.info(e)
            res = {'status':False,'message':"Server Error",'data':[]}
            return JsonResponse(res,status=status.HTTP_400_BAD_REQUEST)
        
    def delete(self,request):
        #API FOR DETELE THE TASK
        try:
            ID_ = request.query_params.get('id')
            task_obj = Task.objects.filter(id=int(ID_),created_by_id=request.user.id).last()
            
            if task_obj == None or not ID_:
                res = {'status':False,'message':'Task not found','data':[]}
                return Response(res,status=status.HTTP_400_BAD_REQUEST)
            
            Task.objects.filter(id=int(ID_)).delete()
            
            res = {'status':True,'message':'Task deleted successfully','data':[]}
            return Response(res,status=status.HTTP_200_OK)
            
        except Exception as e:
            logging.info(e)
            res = {'status':False,'message':"Server Error",'data':[]}
            return JsonResponse(res,status=status.HTTP_400_BAD_REQUEST)
        

    
class Login(APIView):
    permission_classes = [permissions.AllowAny]
    
    def post(self,request):
        try:
            email= request.data['email']          
            password = request.data['password']
            
            if email == None:
                res = {'status':False,'message':"Please enter the keys",'data':[]}
                return Response(res,status=status.HTTP_400_BAD_REQUEST)
            if password == None:
                res = {'status':False,'message':"Please enter password",'data':[]}
                return Response(res,status=status.HTTP_400_BAD_REQUEST)

            email = User.objects.filter(email=email).exists() 
            if not email:
                res = {'status':False,'message':"Please enter valid email",'data':[]}
                return Response(res,status=status.HTTP_400_BAD_REQUEST)
            
            email = User.objects.filter(email=request.data['email']).last()

            user = authenticate(request, email=email.email, password=password)
                                            
            if user is None:
                res = {'status':False,'message':"Incorrect Password",'data':[],'screen_staus':None}
                return Response(res,status = status.HTTP_400_BAD_REQUEST) 
            
                        
            user_data = login_details(user)
            res = {'status':True,'message':"Logged in successfully",'data':[user_data]}
            return Response(res,status=status.HTTP_200_OK)
        
        
        except Exception as e:
            logging.info(e)
            res = {'status':False,'message':"Server Error",'data':[]}
            return JsonResponse(res,status=status.HTTP_400_BAD_REQUEST)
            
