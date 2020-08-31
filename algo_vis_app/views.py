from django.shortcuts import render
from django.views.generic import View

from rest_framework.views import APIView
from rest_framework.response import Response

arr1 = [1,5,3,7,3,23,67]
arr2 = [3,5,5,19,192,192]

def home(request):
	return render(request, 'algo_vis_app/home.html')

class ChartData(APIView): 
    
   
    def get(self, request, format = None): 
        labels = [ 
            '0', 
            '1',  
            '2',  
            '3',  
            '4',  
            '5',  
            '6'
            ] 
        chartLabel = "Bubble Sort Algorithm"
        chartdata = [25, 10, 5, 2, 20, 30, 45] 
        data ={ 
                     "labels":labels, 
                     "chartLabel":chartLabel, 
                     "chartdata":chartdata, 
             } 
        return Response(data)
