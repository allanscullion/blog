#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

# This file is only used if you use `make publish` or
# explicitly specify it as your config file.

import os
import sys
sys.path.append(os.curdir)
from pelicanconf import *

SITEURL = 'https://ascullion.com'
RELATIVE_URLS = False

FEED_ALL_ATOM = 'feeds/all.atom.xml'
CATEGORY_FEED_ATOM = 'feeds/%s.atom.xml'

DIRECT_TEMPLATES = ('index', 'categories', 'authors', 'archives', 'search', 'tags')

THEME = '../pelican-themes/pelican-bootstrap3'
#BOOTSTRAP_THEME = 'cerulean'
#BOOTSTRAP_THEME = 'cosmo'
#BOOTSTRAP_THEME = 'flatly'
#BOOTSTRAP_THEME = 'simplex'
BOOTSTRAP_THEME = 'yeti'
BOOTSTRAP_FLUID = False

PLUGIN_PATHS = ["../pelican-plugins"]

PLUGINS = ['i18n_subsites', 'tag_cloud', 'tipue_search', ]

JINJA_ENVIRONMENT = {
            'extensions': ['jinja2.ext.i18n'],
            }

DELETE_OUTPUT_DIRECTORY = True
DISPLAY_PAGES_ON_MENU = True
DISPLAY_CATEGORIES_ON_MENU = False

# Following items are often useful when publishing

DISQUS_SITENAME = "allanscullion"
DISQUS_DISPLAY_COUNTS = True

GITHUB_USER = 'allanscullion'
GITHUB_SHOW_USER_LINK = True

GOOGLE_ANALYTICS = "UA-55672362-1"

TAGS_URL = "tags.html"

PAGE_ORDER_BY = 'sortorder'
PAGES_SORT_ATTRIBUTE = 'sortorder'
DISPLAY_BREADCRUMBS = False
DEFAULT_PAGINATION = 3

DEFAULT_DATE_FORMAT = '%a %d %B %Y'
DEFAULT_CATEGORY = 'Misc'

ARTICLE_URL = '{date:%Y}/{date:%m}/{date:%d}/{slug}/'
ARTICLE_SAVE_AS = '{date:%Y}/{date:%m}/{date:%d}/{slug}/index.html'

MONTH_ARCHIVE_SAVE_AS = '{date:%Y}/{date:%m}/index.html'
YEAR_ARCHIVE_SAVE_AS = '{date:%Y}/index.html'

SUMMARY_MAX_LENGTH = None
DISPLAY_RECENT_POSTS_ON_SIDEBAR = True
DISPLAY_ARCHIVE_ON_SIDEBAR = True
DISPLAY_TAGS_ON_SIDEBAR = True
DISPLAY_TAGS_INLINE = True
TAG_CLOUD_MAX_ITEMS = 10

TYPOGRIFY = True


CC_LICENSE = 'CC-BY-NC-SA'
