from django.contrib import admin

from recipes.models import (Ingredient, Recipe,
                            Favorite, Tag,
                            IngredientRecipe,
                            ShoppingCart)


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'slug', 'color')
    list_editable = ('color',)
    list_display_links = ('name',)
    search_fields = ('name',)


@admin.register(Ingredient)
class IngredientAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'measurement_unit')
    list_filter = ('name', )
    list_display_links = ('name',)
    search_fields = ('name',)
    empty_value_display = '-пусто-'


class RecipeIngredientInline(admin.TabularInline):
    model = Recipe.ingredients.through
    extra = 1


@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    inline = (RecipeIngredientInline, )
    list_display = ('id', 'name', 'author',
                    'text', 'cooking_time',
                    'pub_date', 'image')
    search_fields = ('name', 'author', 'tags')
    list_filter = ('name', 'author', 'tags', 'pub_date')
    ordering = ('-pub_date',)
    readonly_fields = ('favorite_count', 'pub_date')
    list_display_links = ('name',)
    empy_value_display = '-пусто-'

    @admin.display(description='Сколько раз добавлено в избранное:')
    def favorite_count(self, recipe):
        return recipe.favorites_recipe.count()


@admin.register(IngredientRecipe)
class IngredientRecipeAdmin(admin.ModelAdmin):
    list_display = ('id', 'recipe',
                    'ingredient', 'amount')
    search_fields = ('recipe',)
    list_display_links = ('recipe',)
    empy_value_display = '-пусто-'


@admin.register(Favorite)
class FavoriteAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'recipe')
    search_fields = ('user',)
    list_display_links = ('user',)
    empy_value_display = '-пусто-'


@admin.register(ShoppingCart)
class ShoppingCartAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'recipe')
    search_fields = ('user',)
    list_display_links = ('user',)
    empy_value_display = '-пусто-'
