from django.urls import path
from mainapp.views import ProductDetail, ProductListView

app_name = 'mainapp'
urlpatterns = [
    path('', ProductListView.as_view(), name='products'),
    path('category/<int:id_category>/', ProductListView.as_view(), name='category'),
    path('page/<int:page>/', ProductListView.as_view(), name='page'),
    path('detail/<int:pk>/', ProductDetail.as_view(), name='detail')
]
