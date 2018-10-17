from django.db import models


class CurrentCongress(models.Model):
    last_name = models.TextField(blank=True, null=True)
    first_name = models.TextField(blank=True, null=True)
    middle_name = models.TextField(blank=True, null=True)
    suffix = models.TextField(blank=True, null=True)
    nickname = models.TextField(blank=True, null=True)
    full_name = models.TextField(blank=True, null=True)
    birthday = models.TextField(blank=True, null=True)
    gender = models.TextField(blank=True, null=True)
    type = models.TextField(blank=True, null=True)
    state = models.TextField(blank=True, null=True)
    district = models.TextField(blank=True, null=True)
    senate_class = models.IntegerField(blank=True, null=True)
    party = models.TextField(blank=True, null=True)
    url = models.TextField(blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    phone = models.TextField(blank=True, null=True)
    contact_form = models.TextField(blank=True, null=True)
    rss_url = models.TextField(blank=True, null=True)
    twitter = models.TextField(blank=True, null=True)
    facebook = models.TextField(blank=True, null=True)
    youtube = models.TextField(blank=True, null=True)
    youtube_id = models.TextField(blank=True, null=True)
    bioguide_id = models.TextField(blank=True, null=True)
    thomas_id = models.IntegerField(blank=True, null=True)
    opensecrets_id = models.TextField(blank=True, null=True)
    lis_id = models.TextField(blank=True, null=True)
    fec_ids = models.TextField(blank=True, null=True)
    cspan_id = models.IntegerField(blank=True, null=True)
    govtrack_id = models.IntegerField(blank=True, null=True)
    votesmart_id = models.IntegerField(blank=True, null=True)
    ballotpedia_id = models.TextField(blank=True, null=True)
    washington_post_id = models.TextField(blank=True, null=True)
    icpsr_id = models.IntegerField(blank=True, null=True)
    wikipedia_id = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.full_name

