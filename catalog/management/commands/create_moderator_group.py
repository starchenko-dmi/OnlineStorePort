# your_app/management/commands/create_moderator_group.py
from django.core.management.base import BaseCommand
from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType
from catalog.models import Product  # замените your_app на имя вашего приложения

class Command(BaseCommand):
    help = 'Создаёт группу «Модератор продуктов» с необходимыми разрешениями'

    def handle(self, *args, **options):
        # Получаем content type для модели Product
        product_content_type = ContentType.objects.get_for_model(Product)

        # Получаем или создаём разрешение can_unpublish_product
        unpublish_perm, created = Permission.objects.get_or_create(
            codename='can_unpublish_product',
            name='Может отменять публикацию продукта',
            content_type=product_content_type,
        )

        # Получаем разрешение на удаление
        delete_perm = Permission.objects.get(
            codename='delete_product',
            content_type=product_content_type,
        )

        # Создаём или получаем группу
        group, created = Group.objects.get_or_create(name='Модератор продуктов')

        # Назначаем разрешения
        group.permissions.set([unpublish_perm, delete_perm])
        group.save()

        if created:
            self.stdout.write(
                self.style.SUCCESS('Группа «Модератор продуктов» успешно создана и настроена.')
            )
        else:
            self.stdout.write(
                self.style.WARNING('Группа «Модератор продуктов» уже существовала. Разрешения обновлены.')
            )