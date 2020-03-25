import os
from shutil import copyfile

from bs4 import BeautifulSoup
from django.core.management import BaseCommand

from project.settings import BASE_DIR


class Command(BaseCommand):
    def handle(self, *args, **options):
        file = os.path.join(BASE_DIR, 'frontend', 'dist', 'index.html')
        new_file = os.path.join(BASE_DIR, 'templates', 'index.html')
        copyfile(file, new_file)
        index_file = open(new_file, 'r')
        content = index_file.read()

        def djangolize_link(lnk):
            return "{% static '" + lnk.replace('/static/', '') + "' %}"

        soup = BeautifulSoup(content, 'html.parser')
        index_file.close()
        lnks = soup.find_all('link')
        scripts = soup.find_all('script')
        imgs = soup.find_all('img')
        for lnk in lnks:
            if lnk.get('href') and "{% static '" not in lnk.get('href'):
                lnk['href'] = djangolize_link(lnk['href'])
        for sc in scripts:
            if sc.get('src') and "{% static '" not in sc.get('src'):
                sc['src'] = djangolize_link(sc['src'])
        for im in imgs:
            if im.get('src') and "{% static '" not in im.get('src'):
                im['src'] = djangolize_link(im['src'])
        p_header = '{% load static %}'
        content = (p_header if p_header not in content else '') + str(soup)
        index_file = open(new_file, 'w')
        index_file.write(content)
        index_file.close()
