from django.core.management.base import BaseCommand
from civics.models import CurrentCongress
import csv


def parse_csv():
    data = []
    with open(r'C:\Users\Colton\Downloads\legislators-current.csv', newline='') as csvfile:
        lines = csv.reader(csvfile, delimiter=',', quotechar='"')
        for i, row in enumerate(lines):
            if i == 0:
                headers = row
                continue
            row_data = {}
            for v in range(len(headers)):
                row_data[headers[v]] = row[v]
            data.append(row_data)
    return data


class Command(BaseCommand):

    def handle(self, *args, **options):
        data = parse_csv()
        for datum in data:
            # get or create if it doesn't exist
            first_name = datum['first_name']
            last_name = datum['last_name']
            middle_name = datum['middle_name']
            suffix = datum['suffix']
            nickname = datum['nickname']
            birthday = datum['birthday']
            gender = datum['gender']
            house = datum['type']
            state = datum['state']
            district = datum['district']
            senate_class = datum['senate_class']
            party = datum['party']
            url = datum['url']
            address = datum['address']
            phone = datum['phone']
            contact_form = datum['contact_form']
            rss_url = datum['rss_url']
            twitter = datum['twitter']
            facebook = datum['facebook']
            youtube = datum['youtube']
            youtube_id = datum['youtube_id']
            bioguide_id = datum['bioguide_id']
            thomas_id = datum['thomas_id']
            opensecrets_id = datum['opensecrets_id']
            lis_id = datum['lis_id']
            fec_ids = datum['fec_ids']
            cspan_id = datum['cspan_id']
            govtrack_id = datum['govtrack_id']
            votesmart_id = datum['votesmart_id']
            ballotpedia_id = datum['ballotpedia_id']
            washington_post_id = datum['washington_post_id']
            wikipedia_id = datum['wikipedia_id']

            if senate_class == '':
                senate_class = None
            if thomas_id == '':
                thomas_id = None
            if cspan_id == '':
                cspan_id = None
            if govtrack_id == '':
                govtrack_id = None
            if votesmart_id == '':
                votesmart_id = None

            if CurrentCongress.objects.filter(first_name=first_name, last_name=last_name).count() == 0: # check if the record exists
                cc = CurrentCongress(first_name=first_name,
                                        last_name=last_name,
                                        middle_name=middle_name,
                                        suffix=suffix,
                                        nickname=nickname,
                                        birthday=birthday,
                                        gender=gender,
                                        house=house,
                                        state=state,
                                        district=district,
                                        senate_class=senate_class,
                                        party=party,
                                        url=url,
                                        address=address,
                                        phone=phone,
                                        contact_form=contact_form,
                                        rss_url=rss_url,
                                        twitter=twitter,
                                        facebook=facebook,
                                        youtube=youtube,
                                        youtube_id=youtube_id,
                                        bioguide_id=bioguide_id,
                                        thomas_id=thomas_id,
                                        opensecrets_id=opensecrets_id,
                                        lis_id=lis_id,
                                        fec_ids=fec_ids,
                                        cspan_id=cspan_id,
                                        govtrack_id=govtrack_id,
                                        votesmart_id=votesmart_id,
                                        ballotpedia_id=ballotpedia_id,
                                        washington_post_id=washington_post_id,
                                        wikipedia_id=wikipedia_id)  # create the record if it doesn't exist
                cc.save()