import os
import django
from faker import Faker


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mystore.settings')
django.setup()

from comments.models import Comment
from elements.models import Element


def main():
    faker = Faker()

    elements = list(Element.objects.all())
    if not elements:
        print('No hay elementos creados. Crea al menos un Element antes de generar comentarios.')
        return

    created_count = 0
    for _ in range(5):
        Comment.objects.create(
            text=faker.sentence(nb_words=12),
            element=faker.random_element(elements),
        )
        created_count += 1

    print(f'Se crearon {created_count} comentarios de prueba.')


if __name__ == '__main__':
    main()