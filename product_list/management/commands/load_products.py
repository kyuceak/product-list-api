import os
import json
from django.conf import settings
from django.core.management.base import BaseCommand
from product_list.models import Product

class Command(BaseCommand):
    help = "Load products from product.json into the database."

    def handle(self, *args, **options):
        # Construct the path using BASE_DIR
        file_path = os.path.join(settings.BASE_DIR, 'products.json')
        if not os.path.exists(file_path):
            self.stdout.write(self.style.ERROR(f"{file_path} not found."))
            return

        with open(file_path, 'r') as file:
            products_data = json.load(file)

        for item in products_data:
            Product.objects.create(
                name=item.get("name"),
                popularity_score=item.get("popularityScore"),
                weight=item.get("weight"),
                images=item.get("images")
            )
        self.stdout.write(self.style.SUCCESS("Successfully loaded products."))
