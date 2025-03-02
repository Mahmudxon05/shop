from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from django_filters import rest_framework as filters
from rest_framework.response import Response
from rest_framework import generics, status
from .serializers import *
from .views import *
from .filters import *
#----------------------------GET_FUCTION-----------------------------#
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def product_view(request):
    products = Product.objects.all()
    color = request.query_params.get('color')
    price = request.query_params.get('price')
    if color is not None:
        products = Product.objects.filter(colors = color)        
    if price is not None:
        products = Product.objects.filter(price = price)
    ser = ProductSerializer(products, many=True)
    return Response(ser.data)


@api_view(['GET'])
def category_view(request):
    cats = Category.objects.all()
    queryset = ProductFilter(request.GET, queryset=cats)
    res = CategorySerializer(cats, many = True)
    return Response(res.data)


@api_view(['GET'])
def sub_category_view(request):
    subcat = SubCategory.objects.all()
    res = SubCategorySerializer(subcat, many = True)
    return Response(res.data)


@api_view(['GET'])
def root_category_view(request):
    rutcat = RootCategory.objects.all()
    res = RootCategorySerializer(rutcat, many = True)
    return Response(res.data)


@api_view(['GET'])
def size_view(request):
    size = Size.objects.all()
    res = SizeSerializer(size, many = True)
    return Response(res.data)


@api_view(['GET'])
def color_view(request):
    color = Color.objects.all()
    res = ColorSerializer(color, many = True)
    return Response(res.data)


api_view(['GET'])
def delete_color_view(request,pk):
    color = Color.objectsget(id=pk)
    color.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_cart(request,pk):
    user = request.user
    product = Product.objects.get(id=pk)
    quantity = request.POST.get('quantity')
    cart = Cart.objects.create(user=user, product=product, quantity=quantity)
    ser = CartSerializer(cart)
    return Response(ser.data, status=status.HTTP_201_CREATED)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def create_order(request):
    user = request.user
    total = 0
    order = Order.objects.create(user=user, total=total)
    cart = Cart.objects.filter(user=user)
    for item in cart:
        OrderItem.objects.create(
            product = item.product,
            oreder = order,
            quantity = item.quantity,
            price = item.product.price)
        order.total += item.quantity * item.product.price
        order.save()
    Cart.objects.filter(user=user).delete()
    return Response(OrderSerializer(order).data) 

@api_view(['GET']) 
@permission_classes([IsAuthenticated])
def order_item_view(request,pk):
    order = Order.objects.get(id=pk) 
    items = OrderItem.objects.filter(order=order)
    if order.user == request.user:
        return Response(OrderItemSreializer(items, many=True).data)
    else:
        return Response('{message: Sizda bunday raqamli buyurtma mavjud emas:}')
    

class ProductList(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = ProductFilter
    filterset_fields = "__all__"    