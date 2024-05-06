from django.shortcuts import render, redirect
from .models import Family
from .forms import FamilyForm
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import Family
from .serializers import FamilySerializer
from rest_framework.renderers import JSONRenderer
import io
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.views import View


def family_list(request):
    families = Family.objects.all()
    return render(request, 'family_list.html', {'families': families})

def add_family(request):
    if request.method == 'POST':
        form = FamilyForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('family_list')
    else:
        form = FamilyForm()
    return render(request, 'add_family.html', {'form': form})



@method_decorator(csrf_exempt, name='dispatch')
class FamilyApi(View):
    def post(self, request, *args, **kwargs):
        json_data = request.body
        stream = io.BytesIO(json_data)
        pydata = JSONParser().parse(stream)
        
        serializ = FamilySerializer(data=pydata)
        
        if serializ.is_valid():
            serializ.save()
            resp = {'msg':'data created successfully'}
            return JsonResponse(resp, content_type = "application/json")
        
        json_data = JSONRenderer().render(serializ.errors)
        return HttpResponse(json_data, content_type = "application/json")
    
    def get(self, request, *args, **kwargs):
        json_data = request.body
        stream = io.BytesIO(json_data)
        pydata = JSONParser().parse(stream)
        id = pydata.get('id', None)
        
        if id is not None:
            obj = Family.objects.get(id=id)
            serializ = FamilySerializer(obj)
            return JsonResponse(serializ.data, content_type = "application/json", safe=False)
        
        obj = Family.objects.all()
        serializ = FamilySerializer(obj, many = True)
        return HttpResponse(serializ.data, content_type = "application/json", safe=False)
        
    def put(self, request, *args, **kwargs):
        json_data = request.body
        stream = io.BytesIO(json_data)
        pythondata = JSONParser().parse(stream)
        
        id = pythondata.get('id')
        objec = Family.objects.get(id = id)
        
        serializ = FamilySerializer(objec, data=pythondata, partial = True)

        if serializ.is_valid():
            serializ.save()
            respo = {'msg': 'updated data done.'}
            return JsonResponse(respo,content_type = "application/json" )
        
        return JsonResponse(serializ.errors, content_type = "application/json")
        
    def delete(self, request, *args, **kwargs):
        json_data = request.body
        stream = io.BytesIO(json_data)
        pythondata = JSONParser().parse(stream)
        
        id = pythondata.get('id')

        objec = Family.objects.get(id= id)
        objec.delete()
        respo = {'msg':'deletion complete.'}
        return JsonResponse(respo, content_type = "application/json")
        