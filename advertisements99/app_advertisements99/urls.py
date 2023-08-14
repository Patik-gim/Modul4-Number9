from django.urls import path
from .views import index, top_sellers, advertisement99_post

urlpatterns = [
    path('', index, name='main-page'),
    path('top-sellers/', top_sellers, name='top-sellers'),
    path('advertisement-post/', advertisement99_post, name='adv-post'),
]