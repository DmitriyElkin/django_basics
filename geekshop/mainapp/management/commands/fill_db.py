import json

from django.core.management.base import BaseCommand

from authapp.models import User
from mainapp.models import ProductCategories, Product


def load_from_json(file_name):
    with open(file_name, 'r', encoding='utf-8') as f:
        return json.load(f)


class Command(BaseCommand):
    def handle(self, *args, **options):
        User.objects.create_superuser(username='dima', email='mail@mail.ru', password='1')

        categories = load_from_json('mainapp/fixtures/cat.json')

        ProductCategories.objects.all().delete()
        for category in categories:
            cat = category.get('fields')
            cat['id'] = category.get('pk')
            new_category = ProductCategories(**cat)
            new_category.save()

        products = load_from_json('mainapp/fixtures/product.json')

        Product.objects.all().delete()
        for product in products:
            prod = product.get('fields')
            cat_id = prod.get('category')
            _category = ProductCategories.objects.get(id=cat_id)
            prod['category'] = _category
            new_category = Product(**prod)
            new_category.save()
