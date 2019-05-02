# from rest_framework import viewsets, permissions
# import json
# import os
# from django.core.management.base import BaseCommand
# from datetime import datetime
# from data_service.settings import BASE_DIR

# class Command(BaseCommand):
#     def json_reader(self):
#         f = open('path_to_file.json')
#         json_string = f.read()
#         f.close()

#         data = json.loads(json_string)
#         return data
    
#     def handle(self, *args, **options):
#         """
#         Call the function to import data
#         """
#         self.json_reader()