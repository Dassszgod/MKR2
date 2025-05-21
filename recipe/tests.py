from django.test import TestCase

# Create your tests here.

from django.test import TestCase
from django.urls import reverse
from .models import Category, Recipe

class RecipeViewsTest(TestCase):
    def setUp(self):
        self.category = Category.objects.create(name="Desserts")
        self.recipe = Recipe.objects.create(
            title="Chocolate Cake",
            description="Delicious and rich",
            instructions="Mix and bake",
            ingredients="flour, sugar, cocoa",
            category=self.category,
        )

    def test_main_view_status_code(self):
        url = reverse('main')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Recipes")
        self.assertContains(response, self.recipe.title)

    def test_category_detail_view_status_code(self):
        url = reverse('category_detail', args=[self.category.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.recipe.title)

    def test_category_detail_view_empty(self):
        empty_category = Category.objects.create(name="Empty Category")
        url = reverse('category_detail', args=[empty_category.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "No recipes found.")

