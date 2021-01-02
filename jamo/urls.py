from django.urls import path, include
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework import routers
from jamo import views

router = routers.DefaultRouter()
router.register('myverbs', views.MyverbsView)

# The API URLs are now determined automatically by the router.
urlpatterns = [
    path('', include(router.urls)),
    path('verbs/<str:level>/', views.snippet_list),   
    path('myverbs12/', views.get_my_verbs),   
    path('username/', views.check_username),   
]

 