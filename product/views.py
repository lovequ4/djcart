from django.http import Http404
from .serializers import ProductSerializer,CategorySerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Product,Category
from django.db.models import Q

@api_view(['GET'])
def LatestProduct(request):
    products = Product.objects.all()
    serializer = ProductSerializer(products, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def ProductDetail(request, category_slug, product_slug):
    def get_object(category_slug, product_slug):
        try:
            return  Product.objects.filter(category__slug=category_slug).get(slug=product_slug)
        except Product.DoesNotExist:
            raise Http404

    product = get_object(category_slug, product_slug)
    serializer = ProductSerializer(product)
    return Response(serializer.data)    


@api_view(['GET'])
def CategoryDetail(request, category_slug):
    def get_object(category_slug):
        try:
            return  Category.objects.get(slug=category_slug)
        except Category.DoesNotExist:
            raise Http404

    category = get_object(category_slug)
    serializer = CategorySerializer(category)
    return Response(serializer.data)   


@api_view(['POST'])
def Search(request):
    query = request.data.get('query', '')

    if query:
        products = Product.objects.filter(Q(name__icontains=query) | Q(description__icontains=query))
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)
    else:
        return Response({"products": []})