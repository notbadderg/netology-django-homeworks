import csv

from django.core.management.base import BaseCommand
from django.template.defaultfilters import slugify
from phones.models import Phone


class Command(BaseCommand):
    help = f'Imports phones from "phones.csv" or (if specified with -f) from other file.'

    def add_arguments(self, parser):
        parser.add_argument(
            '-f',
            '--file',
            action='store',
            default='phones.csv',
            help='*.csv file contains phones'
        )

    def handle(self, *args, **options):
        with open(options['file'], 'r') as file:
            phones = list(csv.DictReader(file, delimiter=';'))

        for phone in phones:
            Phone.objects.create(
                id=phone['id'],
                name=phone['name'],
                price=phone['price'],
                image=phone['image'],
                release_date=phone['release_date'],
                lte_exists=phone['lte_exists'],
                slug=slugify(phone['name'])
            )
