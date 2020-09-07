from django.shortcuts import render
from django.views.generic import View

from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import HttpResponse
from django.http import JsonResponse
import sys
import pathlib
import json
from algo_vis_app.SortingAlgorithms.BubbleSort import bubble_sort
# @APIView(('GET',))
# @renderer_classes((TemplateHTMLRenderer, JSONRenderer))



def Bubble_Sort(request):
	array_data = request.POST['nums_array[]']
	data = json.loads(array_data)
	print("test")
	print("data: ",data)
	algo_info = bubble_sort(data)
	print("reached bubble_sort view function")
	print("algo_info: ",algo_info)
	# return HttpResponse(request,'algo_vis_app/home.html',{"algo_info":algo_info})
	# return HttpResponse(algo_info)
	
	# return HttpResponse({"algo_info":algo_info})
	return JsonResponse({"algo_info":algo_info})


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
        chartLabel = "Choose an Algorithm!"
        chartdata = [25, 10, 5, 2, 20, 30, 45] 
        data ={ 
                     "labels":labels, 
                     "chartLabel":chartLabel, 
                     "chartdata":chartdata, 
             } 
        return Response(data)



