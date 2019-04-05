import json
import os
import django

#
# OWASP Top 10 labels loader.
#

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "sh00t.settings")
django.setup()

from sh00t.models import Label

owasp_file = open('data/owasp_top10_label.json', 'r')
label_json = json.load(owasp_file)
for label in label_json['labels']:
    new_label = Label(title=label["title"], color=label["color"])
    new_label.save()
print("OWASP 2017 Top 10 labels has been imported !")
