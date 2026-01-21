from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TagViewSet, PieceTypeViewSet, ItemViewSet

# 1. Initialize the Router
router = DefaultRouter()

# 2. Register the ViewSets
# This automatically creates /tags/, /tags/{id}/, etc.
router.register(r'tags', TagViewSet, basename='tag')
router.register(r'piece-types', PieceTypeViewSet, basename='piece-type')
router.register(r'items', ItemViewSet, basename='item')

# 3. Define the app's URL patterns
urlpatterns = [
    path('', include(router.urls)),
]