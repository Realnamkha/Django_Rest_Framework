from rest_framework import serializers
from rest_framework.reverse import reverse
from products.models import Product
from .validators import unique_product_title,validate_title_no_hello
from api.serializers import UserPublicSerializer


class ProductInlineSerializer(serializers.Serializer):
    url = serializers.HyperlinkedIdentityField(
            view_name='product-detail',
            lookup_field='pk',
            read_only=True
    )
    title = serializers.CharField(read_only=True)

class ProductSerializer(serializers.ModelSerializer):
    owner = UserPublicSerializer(source="user",read_only=True)
    # my_user_data = serializers.SerializerMethodField(read_only=True)
    # related_products = ProductInlineSerializer(source='user.product_set.all', read_only=True, many=True)
    # my_discount = serializers.SerializerMethodField(read_only=True)
    # url = serializers.SerializerMethodField(read_only=True)
    url = serializers.HyperlinkedIdentityField(
        view_name='product-detail',
        lookup_field = 'pk')
    title = serializers.CharField(validators=[unique_product_title,validate_title_no_hello])
    # email = serializers.EmailField(write_only=True)
    class Meta:
        model = Product
        fields = [
            'owner',
            'pk',
            'url',
            'title',
            'content',
            'price',
            'sale_price',
            'public'
            # 'my_discount',
            # 'my_user_data',
            # 'related_products'
        ]
    
    def get_my_user_data(self, obj):
        return {
            "username": obj.user.username
        }
    
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

    # def get_my_discount(self, obj):
    #     if not hasattr(obj, 'id'):
    #         return None
    #     if not isinstance(obj, Product):
    #         return None
    #     return obj.get_discount()