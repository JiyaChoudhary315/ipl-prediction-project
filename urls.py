from django.urls import path,include
from .views import PredictMatch

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('prediction.urls')),
]


