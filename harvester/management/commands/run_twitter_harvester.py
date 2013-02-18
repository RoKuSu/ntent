from django.core.management.base import BaseCommand, CommandError
from harvester.twitter import TwitterHarvester


class Command(BaseCommand):
    args = ''
    help = ''

    def handle(self, *args, **options):
        h = TwitterHarvester()
        h.run()
