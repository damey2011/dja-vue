import os

from django.conf import settings
from django.core.management import BaseCommand

from project.settings import BASE_DIR


class Command(BaseCommand):
    def update_static_url(self):
        file = os.path.join(BASE_DIR, 'frontend', 'vue.config.js')
        new_content = ''
        with open(file, 'r') as f:
            for line in f.readlines():
                line = line.strip('\n')
                if 'const ASSET_DIR =' in line:
                    asset_dir = settings.STATIC_URL.lstrip('/').rstrip('/')
                    new_content += line.replace(line, f"const ASSET_DIR = '{asset_dir}';")
                else:
                    new_content += line
                new_content += '\n'

        with open(file, 'w+') as f:
            f.write(new_content)

    def handle(self, *args, **options):
        self.update_static_url()
        print('*' * 100)
        print('Updated static url in vue.config.js to match django for frontend building.')
        print('*' * 100)
        print('\n\n')