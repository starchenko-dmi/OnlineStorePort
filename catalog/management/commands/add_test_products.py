from django.core.management.base import BaseCommand
from catalog.models import Category, Product


class Command(BaseCommand):
    help = 'Удаляет все данные из Category и Product, затем добавляет тестовые записи'

    def handle(self, *args, **options):
        # Удаляем все продукты (сначала — чтобы избежать ошибок внешнего ключа)
        Product.objects.all().delete()
        # Удаляем все категории
        Category.objects.all().delete()

        self.stdout.write(self.style.SUCCESS('Все данные удалены.'))

        # Создаём категории
        electronics = Category.objects.create(
            name="Электроника",
            description="Современные гаджеты и техника"
        )
        books = Category.objects.create(
            name="Книги",
            description="Художественная и образовательная литература"
        )
        clothing = Category.objects.create(
            name="Одежда",
            description="Повседневная и спортивная одежда"
        )

        self.stdout.write('Созданы категории.')

        # Создаём продукты
        products = [
            Product(
                name="Ноутбук UltraBook",
                description="Лёгкий и мощный ноутбук для работы и учёбы",
                purchase_price=65000.00,
                category=electronics
            ),
            Product(
                name="Кроссовки SportRun",
                description="Удобные кроссовки для бега и повседневной носки",
                purchase_price=7500.00,
                category=clothing
            ),
            Product(
                name="Роман 'Мастер и Маргарита'",
                description="Классика русской литературы",
                purchase_price=600.00,
                category=books
            ),
        ]

        Product.objects.bulk_create(products)
        self.stdout.write(self.style.SUCCESS(f'Создано {len(products)} тестовых продуктов.'))