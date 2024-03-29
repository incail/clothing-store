from http import HTTPStatus

from django.test import TestCase
from django.urls import reverse

from .models import Product, ProductCategory


class IndexViewTestCase(TestCase):

    def test_index(self):
        path = reverse('index')
        response = self.client.get(path)
        self.assertEquals(response.status_code, HTTPStatus.OK)
        self.assertEquals(response.context_data['title'], 'Store')
        self.assertTemplateUsed(response, 'products/index.html')


class ProductsListViewTestCase(TestCase):
    fixtures = ['categories.json', 'p2.json']

    def setUp(self):
        self.products = Product.objects.all()

    def test_list(self):
        path = reverse('products:index')
        response = self.client.get(path)

        self._common_test(response)
        self.assertEquals(list(response.context_data['object_list']), list(self.products[:3]))

    def test_list_with_category(self):
        category = ProductCategory.objects.first()
        path = reverse('products:category', kwargs={'category_id': category.id})
        response = self.client.get(path)
        self._common_test(response)
        self.assertEquals(
            list(response.context_data['object_list']),
            list(self.products.filter(category_id=category.id)[:3])
        )

    def _common_test(self, response):
        self.assertEquals(response.status_code, HTTPStatus.OK)
        self.assertEquals(response.context_data['title'], 'Store - Каталог')
        self.assertTemplateUsed(response, 'products/products.html')
