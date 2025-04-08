"""
load the vendors from vendors.json
IMPORTANT
TO RUN, in the terminal, type: 
python manage.py load_the_vendors 

for reference: https://docs.djangoproject.com/en/5.1/howto/custom-management-commands/ 
"""
import json
from django.core.management.base import BaseCommand
from polls.models import Vendor


class Command(BaseCommand):
    help="Use to load vendors from a JSON file filename is load_the_vendors"

    def handle(self, *args,**kwargs):
        #open json file and read the contents 
        with open('polls/vendors.json','r') as aFile: #for this to work, vendors.json has to be in polls directory
            vendors_from_json_file = json.load(aFile)

        #loop through every vendor in the file and create vendor objects 
        for vendor in vendors_from_json_file: 
            Vendor.objects.get_or_create(name=vendor["name"]) #checks if a vendor with the given name already exists, if yea, does nothing, if no then it creates a new Vendor obj with the name

        self.stdout.write(self.style.SUCCESS('Sucess, vendors loaded!'))