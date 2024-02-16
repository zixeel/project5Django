from django.core.management import BaseCommand

from mainapp.models import Student


class Command(BaseCommand):
    def handle(self, *args, **options):
        student_list = [
            {'last_name': 'karl', 'first_name': 'parson'},
            {'last_name': 'steve', 'first_name': 'white'},
            {'last_name': 'alex', 'first_name': 'black'},
            {'last_name': 'jim', 'first_name': 'smith'},
        ]
        # for student_item in student_list:
        #     Student.objects.create(**student_item)
        students_for_create = []

        for student_item in student_list:
            students_for_create.append(
                Student(**student_item)
            )
        print(students_for_create)

        Student.objects.bulk_create(students_for_create)

