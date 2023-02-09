from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from . import views


from drf_yasg import openapi
from drf_yasg.views import get_schema_view


schema_view = get_schema_view(
    openapi.Info(
        title="FoodTales Api",
        default_version='v1',
        description="FoodTalesApi",
        contact=openapi.Contact(email="sultanbek9899@gmail.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
)


urlpatterns = [
    path('docs/', schema_view.with_ui("swagger")),
    path("products/", views.ProductListAPIView.as_view()),
    path("shop/categories/", views.ShopCategoryListAPIView.as_view()),

    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]