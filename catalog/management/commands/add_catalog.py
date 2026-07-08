from django.core.management import call_command
from django.core.management.base import BaseCommand
from django.template.defaultfilters import title

from catalog.models import Product, Category

class Command(BaseCommand):
    help = 'Загрузка данных из фикстур'



    def handle(self, *args, **options):
        Product.objects.all().delete()
        Category.objects.all().delete()


        call_command('loaddata', 'categories.json')
        call_command('loaddata', 'Product.json')
        self.stdout.write(self.style.SUCCESS('Данные загружены из фикстур'))
