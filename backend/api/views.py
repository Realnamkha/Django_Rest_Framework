from django.shortcuts import render
import json
from django.http import JsonResponse,HttpResponse
from django.forms.models import model_to_dict
from products.models import Product

# Create your views here.
# def api_home(request,*args,**kwargs):
#     print(request.GET)
#     body = request.body
#     data = {}
#     try:
#         data = json.loads(body)
#     except:
#         pass
#     print(data.keys())
#     data['params'] = dict(request.GET)
#     data['headers'] = dict(request.headers)
#     data['content_type'] = request.content_type
#     return JsonResponse(data)

# @api_view(["GET"])
def api_home(request, *args, **kwargs):
    model_data = Product.objects.all().order_by("?").first()
    data = {}
    if model_data:
        data = model_to_dict(model_data, fields=['id', 'title', 'price', 'sale_price'])
        # data["title"] = model_data.title
        # data["content"] = model_data.content
        # data["price"] = model_data.price
        #model instance (model_data)
        #turn a python dict
        #return Json to my client
    return JsonResponse(data)
    # return HttpResponse(json_data,headers={"content-type":"application/json"})