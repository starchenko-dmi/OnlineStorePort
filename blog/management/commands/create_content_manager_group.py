from django.core.management.base import BaseCommand
from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType
from blog.models import BlogPost  # ← укажите правильный путь

class Command(BaseCommand):
    help = 'Создаёт группу «Контент-менеджер» с правами на управление блогом'

    def handle(self, *args, **options):
        ct = ContentType.objects.get_for_model(BlogPost)

        permissions = [
            Permission.objects.get(codename='add_blogpost', content_type=ct),
            Permission.objects.get(codename='change_blogpost', content_type=ct),
            Permission.objects.get(codename='delete_blogpost', content_type=ct),
        ]
        group, created = Group.objects.get_or_create(name='Контент-менеджер')
        group.permissions.set(permissions)
        group.save()

        if created:
            self.stdout.write(
                self.style.SUCCESS('Группа «Контент-менеджер» успешно создана.')
            )
        else:
            self.stdout.write(
                self.style.WARNING('Группа «Контент-менеджер» уже существовала. Права обновлены.')
            )