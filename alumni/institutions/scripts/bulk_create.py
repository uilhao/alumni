import os
import csv

from collections import defaultdict

from django.db import models
from django.apps import apps

from institutions import models


class BulkCreateManager(object):
    """
    This helper class keeps track of ORM objects to be created for multiple
    model classes, and automatically creates those objects with `bulk_create`
    when the number of objects accumulated for a given model class exceeds
    `chunk_size`.
    Upon completion of the loop that's `add()`ing objects, the developer must
    call `done()` to ensure the final set of objects is created for all models.
    """

    def __init__(self, chunk_size=100):
        self._create_queues = defaultdict(list)
        self.chunk_size = chunk_size

    def _commit(self, model_class):
        model_key = model_class._meta.label
        model_class.objects.bulk_create(self._create_queues[model_key])
        self._create_queues[model_key] = []

    def add(self, obj):
        """
        Add an object to the queue to be created, and call bulk_create if we
        have enough objs.
        """
        model_class = type(obj)
        model_key = model_class._meta.label
        self._create_queues[model_key].append(obj)
        if len(self._create_queues[model_key]) >= self.chunk_size:
            self._commit(model_class)

    def done(self):
        """
        Always call this upon completion to make sure the final partial chunk
        is saved.
        """
        for model_name, objs in self._create_queues.items():
            if len(objs) > 0:
                self._commit(apps.get_model(model_name))


# python manage.py runscript bulk_create  --dir-policy none

def run():
    records = [
        {"name": "One", "title": "One", "avg_gpa": "3.5", "dapip_id": 12030},
        {"name": "One1", "title": "One1", "avg_gpa": "3.9", "dapip_id": 342343},
    ]
    bulk_mgr = BulkCreateManager(chunk_size=20)
    # rows = [
    #     models.InstitutionPage(title="mee", name="eem"),
    #     models.InstitutionPage(title="mee1", name="eem1"),
    #     models.InstitutionPage(title="mee2", name="eem2"),
    # ]
    for row in records:
        bulk_mgr.add(models.InstitutionListingPage(
            title=row['title'],
            intro=row['name'],
        )
        )

    bulk_mgr.done()

    # models.InstitutionListingPage().objects.bulk_create([
    #     models.InstitutionPage(title="mee", name="eem"),
    #     models.InstitutionPage(title="mee1", name="eem1"),
    #     models.InstitutionPage(title="mee2", name="eem2"),
    # ])
    # page = models.InstitutionPage(title="mee", name="eem")

    # models.InstitutionPage(title="mee", name="eem"),
    # models.InstitutionPage(title="mee1", name="eem1"),
    # models.InstitutionPage(title="mee2", name="eem2"),

    # print(apps.get_model("institution"))

# with open('/path/to/file', 'rb') as csv_file:
#     bulk_mgr = BulkCreateManager(chunk_size=20)
#     for row in csv.reader(csv_file):
#         bulk_mgr.add(MyModel(attr1=row['attr1'], attr2=row['attr2']))
#     bulk_mgr.done()

# >> > Category.objects.all().count()
# 2
# >> > Category.objects.bulk_create(
#     [Category(name="God"),
#      Category(name="Demi God"),
#      Category(name="Mortal")]
# )
# [ < Category: God > , < Category: Demi God > , < Category: Mortal > ]
# >> > Category.objects.all().count()


# if __name__ == '__main__':
#     main()
    # bulk_mgr.add(MyModel(attr1=row['attr1'], attr2=row['attr2']))
    # bulk_mgr.done()

    # bulk_create(records)


# os.environ.setdefault("DJANGO_SETTINGS_MODULE", "blog_project.settings")


# with open('csvtest.csv', 'rt') as f:
#     reader = csv.reader(f)
#     my_list = list(reader)

# headings = my_list.pop(0)

# for row in my_list:
#     new_item = {}
#     i = 0
#     for heading in headings:
#         new_item[heading] = row[i]
#         i = i+1
#     new_bookmark = Bookmark()
#     new_bookmark.title = new_item['title']
#     new_bookmark.url = new_item['url']
#     new_bookmark.date_read = new_item['date_read']
#     new_bookmark.notes = new_item['notes']
#     new_bookmark.save()
