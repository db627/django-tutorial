from django.core.management.base import BaseCommand
from myapp.factories import UserFactory
class Command(BaseCommand):
    help = 'Seeds the database with User and Course data'

    def add_arguments(self, parser):
        parser.add_argument(
            '--users',
            type=int,
            help='Number of users to create'
        )


    def handle(self, *args, **kwargs):
        num_users = kwargs['users'] or 100  # Default to 100 if not specified
    
        self.stdout.write('Seeding {} users...'.format(num_users))
        UserFactory.create_batch(num_users)

        self.stdout.write(self.style.SUCCESS('Database seeding complete!'))
