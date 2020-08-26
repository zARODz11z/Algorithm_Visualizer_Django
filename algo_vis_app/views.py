from django.shortcuts import render
import matplotlib.pyplot as plt 
import io
import urllib, base64
input_data = [
	{
		'arr1': [1,5,3,7,3,23,67],
		'arr2': [3,5,5,19,192,192]
	}
]

def home(request):
	#plt.plot(range(10))
	context = {
		'title': 'Bubble Sort',
		'input_data':input_data
	}
	return render(request, 'algo_vis_app/home.html',context)

def about(request):
	return render(request, 'algo_vis_app/about.html')
