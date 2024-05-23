from rest_framework import serializers
from rest_framework.reverse import reverse
from products.models import Product
from .validators import unique_product_title,validate_title_no_hello

class ProductSerializer(serializers.ModelSerializer):
    my_discount = serializers.SerializerMethodField(read_only=True)
    # url = serializers.SerializerMethodField(read_only=True)
    url = serializers.HyperlinkedIdentityField(
        view_name='product-detail',
        lookup_field = 'pk')
    title = serializers.CharField(validators=[unique_product_title,validate_title_no_hello])
    # email = serializers.EmailField(write_only=True)
    class Meta:
        model = Product
        fields = [
            'pk',
            'url',
            'title',
            'content',
            'price',
            'sale_price',
            'my_discount'
        ]
    
    # def validate_title(self,value):
    #     qs = Product.objects.filter(title__exact=value)
    #     if qs.exists():
    #         raise serializers.ValidationError(f"{value} is already a product name")
    #     return value

    # def create(self,validated_data):
    #     return Product.objects.create(**validated_data)
    #     email = validated_data.pop('email')
    #     obj = super().create(validated_data)
    #     print(email,obj)
    #     return obj
    # def update(self,instance,validated_data):
    #     email = validated_data.pop('email')
    #     instance.title = validated_data.get('title')
    #     return instance
    #     return super().update(instance,validated_data)
    
    def get_url(self,obj):
        request = self.context.get('request')
        if request is None:
            return None
        return reverse("product-detail",kwargs={"pk":obj.pk},request=request)

    def get_my_discount(self, obj):
        if not hasattr(obj, 'id'):
            return None
        if not isinstance(obj, Product):
            return None
        return obj.get_discount()