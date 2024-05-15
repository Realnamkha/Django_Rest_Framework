from django.shortcuts import render
import json
from django.http import JsonResponse,HttpResponse
from django.forms.models import model_to_dict
from products.models import Product
from rest_framework.decorators import api_view
from rest_framework.response import Response
from products.serializers import ProductSerializer


#Create your views here.
# def api_home(request,*args,**kwargs):
#     print(request.GET) #url parameters
#     body = request.body # JSON DATA
#     data = {}
#     try:
#         data = json.loads(body) # convert to json
#     except:
#         pass
#     print(data.keys())
#     data['params'] = dict(request.GET) 
#     data['headers'] = dict(request.headers)
#     data['content_type'] = request.content_type
#     return JsonResponse(data)

# @api_view(["GET"])
# def api_home(request, *args, **kwargs):
#     model_data = Product.objects.all().order_by("?").first()
#     data = {}
#     if model_data:
#         data = model_to_dict(model_data, fields=['id', 'title', 'price', 'sale_price'])
#         data["title"] = model_data.title
#         data["content"] = model_data.content
#         data["price"] = model_data.price
#         model instance (model_data)
#         turn a python dict
#         return Json to my client
#     return JsonResponse(data)
#     return HttpResponse(json_data,headers={"content-type":"application/json"})


# @api_view(["GET"])
# def api_home(request, *args, **kwargs):
#     instance = Product.objects.all().order_by("?").first()
#     data = {}
#     if instance:
#         data = ProductSerializer(instance).data
#     return Response(data)

@api_view(["POST"])
def api_home(request, *args, **kwargs):
    serializer = ProductSerializer(data=request.data)
    if serializer.is_valid():
        # instance = serializer.save()
        print(serializer.data)
        return Response(serializer.data)