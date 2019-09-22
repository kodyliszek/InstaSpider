from django.conf import settings
from django.http import HttpResponse
from django.views import View

from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd
import datetime


class TarantulaView(View):
    def get(self, request, phrase=None):
        if phrase:
            tag_list = [phrase]
        else:
            tag_list = self.get_tag_list()

        print(tag_list)
        return HttpResponse('result: {}'.format(tag_list))

    def get_tag_list(self):

        driver = webdriver.Chrome(settings.BASE_DIR + '/tarantula/chromedriver')

        # Extract description of a post from Instagram link
        driver.get('https://www.instagram.com/p/B2t6lgJA2E8/')
        soup = BeautifulSoup(driver.page_source, "lxml")
        desc = " "

        for item in soup.findAll('a'):
            desc = desc + " " + str(item.string)

        # Extract tag list from Instagram post description
        taglist = desc.split()
        taglist = [x for x in taglist if x.startswith('#')]
        index = 0
        while index < len(taglist):
            taglist[index] = taglist[index].strip('#')
            index += 1
        return taglist
