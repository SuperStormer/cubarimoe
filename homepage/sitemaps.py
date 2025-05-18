from django.contrib.sitemaps import Sitemap
from django.shortcuts import reverse

class StaticViewSitemap(Sitemap):
    changefreq = "daily"
    priority = 0.7
    protocol = "https"

    def items(self):
        return ["site-home"]

    def location(self, item):
        return reverse(item)
