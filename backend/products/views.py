from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from .models import Product
from .serializers import ProductSerializer

class ProductListCreateAPIView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    # def perform_create(self,serializer):
    #     # serializer.save(user=self.request.user)
    #     print(serializer)
    #     serializer.save()
    #     # title = serializer.validated_data.get('title')
    #     # content = serializer.validated_data.get('content') or None
    #     # if content is None:
    #     #     content = title
    #     # serializer.save(content=content)


product_listcreate_view = ProductListCreateAPIView.as_view()

class ProductDetailAPIView(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

product_detail_view = ProductDetailAPIView.as_view()

# class ProductListAPIView(generics.RetrieveAPIView):
#     queryset = Product.objects.all()
#     serializer_class = ProductSerializer

# product_list_view = ProductListAPIView.as_view()
@api_view(["POST","GET"])
def product_alt_view(request,pk=None,*args,**kwargs):
    method = request.method
    if method == "GET":
        if pk is not None:
            obj = get_object_or_404(Product,pk=pk)
            data = ProductSerializer(obj,many=False).data
            return Response(data)
        qs = Product.objects.all()
        data = ProductSerializer(qs,many=True).data
        return Response(data)
    
    if method == "POST":
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            title = serializer.validated_data.get('title')
            content = serializer.validated_data.get('content') or None
            if content is None:
                content = title
            serializer.save(content=content)
        return Response(serializer.data)