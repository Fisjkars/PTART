import json
import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "sh00t.settings")
django.setup()

from configuration.models import MethodologyMaster, ModuleMaster, CaseMaster
from app.models import Project, Template

print("This will reset everything in the database and set up as fresh.")
print("Are you wanna do this?")
answer = input("[No] | Yes?\n") or ""
if "yes" == answer.lower():

    Project.objects.all().delete()  # Deleting Project will trigger to delete everything: Flags, Sh0ts, Assessments, Screenshots
    CaseMaster.objects.all().delete()
    ModuleMaster.objects.all().delete()
    MethodologyMaster.objects.all().delete()
    Template.objects.all().delete()

    for filename in os.listdir('screenshots'):
        if filename.endswith('.png'):
            os.remove(os.path.join('screenshots',filename))