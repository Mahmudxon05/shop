from .models import *
from rest_framework.serializers import ModelSerializer
from users.serializers import UserSerializer

#----------------------------   Serializer Classes   -------------------------------#
class RootCategorySerializer(ModelSerializer):
    class Meta:
        model = RootCategory
        fields = '__all__'
        

class SubCategorySerializer(ModelSerializer):
    class Meta:
        model = SubCategory
        fields = '__all__'



class CategorySerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'



class ProductSerializer(ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'



class SizeSerializer(ModelSerializer):
    class Meta:
        model = Size
        fields = '__all__'



class ColorSerializer(ModelSerializer):
    class Meta:
        model = Color
        fields = '__all__'    



class ProductSerializer(ModelSerializer):
    color = ColorSerializer(read_only = True)
    size = SizeSerializer(read_only = True)
    class Meta:
        model = Product
        fields = "__all__"
        depth = 3


class CartSerializer(ModelSerializer):
    user = UserSerializer(read_only = True)
    product = ProductSerializer(read_only = True)
    class Meta:
        model = Cart
        fields = '__all__' 


class OrderSerializer(ModelSerializer):
    user = UserSerializer(read_only = True)
    class Meta:
        model = Order
        fields = ['id','user','total','created_at','status']               


class OrderItemSreializer(ModelSerializer):
    product = ProductSerializer(read_only = True)
    order = OrderSerializer(read_only =True)
    class Meta:
        model = OrderItem
        fields = '__all__'





