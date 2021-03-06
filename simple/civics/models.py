from django.db import models


class CurrentCongress(models.Model):
    last_name = models.TextField(default='')
    first_name = models.TextField(default='')
    middle_name = models.TextField(default='')
    suffix = models.TextField(default='')
    nickname = models.TextField(default='')
    birthday = models.TextField(default='')
    gender = models.TextField(default='')
    house = models.TextField(default='')
    state = models.TextField(default='')
    district = models.TextField(default='')
    senate_class = models.IntegerField(blank=True, null=True)
    party = models.TextField(default='')
    url = models.TextField(default='')
    address = models.TextField(default='')
    phone = models.TextField(default='')
    rss_url = models.TextField(default='')
    twitter = models.TextField(default='')
    facebook = models.TextField(default='')
    contact_form = models.TextField(default='')
    youtube = models.TextField(default='')
    youtube_id = models.TextField(default='')
    bioguide_id = models.TextField(default='')
    thomas_id = models.IntegerField(blank=True, null=True)
    opensecrets_id = models.TextField(default='')
    lis_id = models.TextField(default='')
    fec_ids = models.TextField(default='')
    cspan_id = models.IntegerField(blank=True, null=True)
    govtrack_id = models.IntegerField(blank=True, null=True)
    votesmart_id = models.IntegerField(blank=True, null=True)
    ballotpedia_id = models.TextField(default='')
    washington_post_id = models.TextField(default='')
    wikipedia_id = models.TextField(default='')

    def wiki_link(self):
        return "https://en.wikipedia.org/wiki/"+self.wikipedia_id.replace(' ','_')

    def full_name(self):
        return '{0} {1}'.format(self.first_name, self.last_name)

    def __str__(self):
        return self.last_name

