from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views
from rest_framework_simplejwt.views import (
    TokenRefreshView,
)

urlpatterns = [
    # instructor
    path('getInstructor/', views.getInstructors, name="getinstructors"),
    path('getInstructor/<str:pk>', views.getInstructor, name="getinstructor"),
    path('postInstructor/', views.postInstructor, name="postinstructor"),
    path('putInstructor/<str:pk>', views.putInstructor, name="putinstructor"),
    path('deleteInstructor/<str:pk>', views.deleteInstructor, name="putinstructor"),

    # trainer
    path('getTrainer/', views.getTrainers, name="getTrainers"),
    path('getTrainer/<str:pk>', views.getTrainer, name="getTrainer"),
    path('postTrainer/', views.postTrainer, name="postTrainer"),
    path('putTrainer/<str:pk>', views.putTrainer, name="putTrainer"),
    path('deleteTrainer/<str:pk>', views.deleteTrainer, name="deleteTrainer"),


    # gallery
    path('getGallery/', views.getGallerys, name="getGallerys"),
    path('getGallery/<str:pk>', views.getGallery, name="getGallery"),
    path('postGallery/', views.postGallery, name="postGallery"),
    path('putGallery/<str:pk>', views.putGallery, name="putGallery"),
    path('deleteGallery/<str:pk>', views.deleteGallery, name="deleteGallery"),


    path('api/token/', views.MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/register/', views.RegisterView.as_view(), name='auth_register'),
    path('api/', views.getRoutes),
    path('api/test/', views.testEndPoint, name='test')

]

urlpatterns = format_suffix_patterns(urlpatterns)