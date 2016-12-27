from django.shortcuts import render
from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from django.http import HttpResponse
from clickstream.core.resources import getChartData
# Create your views here.
import json

def dashboard(request):
	return render(request, 'index.html')


def results(request):	
	
	return render(request,'results.html')

def results_data(request):
	data=dict()
	data['result']=getChartData()
	return HttpResponse(json.dumps(data), content_type='application/json')