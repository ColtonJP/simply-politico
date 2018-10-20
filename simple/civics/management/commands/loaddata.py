from django.core.management.base import BaseCommand
from civics.models import CurrentCongress


def parse_csv(path):
    with open(path, 'r') as f:
        lines = f.read().split('\n')
    headers = lines[0].split(',')
    lines.pop(0)
    data = []
    for line in lines:
        if line == '':
            continue
        row_data = {}
        row_data_text = line.split(',')
        for i in range(len(headers)):
            row_data[headers[i]] = row_data_text[i]
        data.append(row_data)
    return data


class Command(BaseCommand):

    def handle(self, *args, **options):

        data = parse_csv(r'C:\Users\Colton\PycharmProjects\simply-politico\simple\civics\management\commands\legislators-current (1).csv')
        for datum in data:
            # get or create if it doesn't exist
            last_name = datum['last_name ']
            if CurrentCongress.objects.filter(name=last_name).count() == 0:
                last_name = CurrentCongress(name=last_name)
                last_name.save()
            else:
                last_name = CurrentCongress.objects.get(name=last_name)
            first_name = datum['first_name']
            if CurrentCongress.objects.filter(name=first_name ).count() == 0:
                first_name = CurrentCongress(name=first_name , last_name=last_name)
                first_name.save()
            else:
                first_name = CurrentCongress.objects.get(name=first_name, currentcongress_id=currentcongress.id)

            fn = CurrentCongress(last_name=last_name, first_namen=first_name)
            fn.save()
