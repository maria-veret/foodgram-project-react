from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import (IngredientViewSet, RecipeViewSet,
                    FavRecipeViewSet, CreateUserViewSet,
                    RecipeCartViewSet, SubscribeViewSet, TagViewSet)

app_name = 'api'
router = DefaultRouter()


router.register('recipes', RecipeViewSet, basename='recipes')
router.register('ingredients', IngredientViewSet, basename='ingredients')
router.register('users', CreateUserViewSet, basename='users')
router.register('tags', TagViewSet, basename='tags')
router.register(
    r'users/(?P<user_id>\d+)/subscribe', SubscribeViewSet,
    basename='subscribe')
router.register(
    r'recipes/(?P<recipe_id>\d+)/favorite', FavRecipeViewSet,
    basename='favorite')
router.register(
    r'recipes/(?P<recipe_id>\d+)/recipe_cart', RecipeCartViewSet,
    basename='recipecart')

urlpatterns = [
    path('', include(router.urls)),
    path('', include('djoser.urls')),
    path('auth/', include('djoser.urls.authtoken')),
]
