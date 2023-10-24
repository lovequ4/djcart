from django.urls import path
from .views import LatestProduct,ProductDetail,CategoryDetail,Search

urlpatterns = [
    path('latest',LatestProduct),
    path('search',Search),
    path('<slug:category_slug>/<slug:product_slug>',ProductDetail),
    path('<slug:category_slug>',CategoryDetail)
]