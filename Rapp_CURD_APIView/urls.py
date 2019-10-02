from django.conf.urls import url
from Rapp_CURD_APIView import views
app_name = "Rapp_CURD_APIView"
urlpatterns = [
    url(r'^product/(?P<pk>[0-9]+)$',views.ProductView.as_view()),
    url(r'^product/(?P<Product_id>[0-9]+)/reviews/(?P<Review_id>[0-9]+)/$'
        ,views.ReviewView.as_view())
]