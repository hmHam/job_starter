import random
import string

from django.utils import timezone
from django.db import connection
from django.db import models

# TODO: 引数からモデルの作成数を指定できるように
COOK_NUMBER = 5

tables = connection.introspection.table_names()
seen_models = connection.introspection.installed_models(tables)

def make_dummy_data(model, cook_number):
    model_data = []
    if model.objects.all().count() >= cook_number:
        # 作成件数に平等性をもたせる
        return []
    for i in range(cook_number):
        for field in model._meta.fields:
            data = {}
            if isinstance(field, models.IntegerField):
                # TODO: Choicesに対応
                data[field.name] = 0
            elif isinstance(field, models.CharField):
                if 'name' in field.name:
                    data[field.name] = 'たろう'
                else:
                    data[field.name] = random.sample(string.ascii_letters, 10)
            elif isinstance(field, models.ForeignKey):
                if field.model.objects.all().exists():
                    data[field.name] = random.choice(
                        field.model.objects.all()
                    ).get()
                else:
                    make_dummy_data(field.model, cook_number)
            elif isinstance(field, models.DateTimeField):
                data[field.name] = timezone.now()
            elif isinstance(field, models.DateField):
                data[field.name] = timezone.today()
            elif isinstance(field, models.BooleanField):
                data[field.name] = random.choice(True, False)
            else:
                # other fields
                pass
            model_data.append(data)
        return model.objects.bulk_create([
            model(**data) for data in model_data
        ])

# DBへのデータ作成
for model in seen_models:
    print('---create-data...!----')
    print('try createing %s....' % model._meta.object_name)
    make_dummy_data(model)

# Fixturesの獲得とdump
fixtures = []
for model in seen_models:
    print('make-fixtures....')
    for m in model.objects.all():
        data = {
            'model': model._meta.db_table.replace('_', '.'),
            'fields': dict(
                [
                    (
                        field.name,
                        getattr(m, field.name)
                    ) for field in model._meta.fields
                ]
            )
        }
        fixtures.append(data)
