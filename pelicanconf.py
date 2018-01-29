#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Allan Scullion'
SITENAME = u'The IT Manager'

SITEURL = ''

PATH = 'content'

TIMEZONE = 'Europe/London'

DEFAULT_LANG = u'en'

PLUGIN_PATHS = ["../pelican-plugins"]

THEME = '../pelican_templates/pelican-bootstrap3'
PYGMENTS_STYLE = 'native'
#BOOTSTRAP_THEME = 'cerulean'
#BOOTSTRAP_THEME = 'cosmo'
#BOOTSTRAP_THEME = 'flatly'
#BOOTSTRAP_THEME = 'simplex'
#BOOTSTRAP_THEME = 'yeti'


# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

# Blogroll
LINKS = 	(
				('Pelican', 'http://getpelican.com/'),
		        ('Python.org', 'http://python.org/'),
        	)

# Social widget
SOCIAL = 	(
	        	('Twitter', 'https://www.twitter.com/allanscullion'),
	        	('LinkedIn', 'https://uk.linkedin.com/in/allanscullion'),
         	)

MENUITEMS =	(
                ('Categories', '/categories.html'),
                ('Tags', '/tags.html'),
                ('Archives', '/archives.html'),
			)

# custom page generated with a jinja2 template
# TEMPLATE_PAGES = {'flickr.html': 'flickr/index.html'}

TAGS_URL = u'tags.html'
BANNER = u'/images/banner.jpg'
BANNER_SUBTITLE = u'They sometimes let me code...'
BANNER_ALL_PAGES = True

PAGE_ORDER_BY = 'sortorder'
DISPLAY_BREADCRUMBS = False
DEFAULT_PAGINATION = 3

DEFAULT_DATE_FORMAT = '%a %d %B %Y'
DEFAULT_CATEGORY = 'Misc'

DISPLAY_PAGES_ON_MENU = True
DISPLAY_CATEGORIES_ON_MENU = True

ARTICLE_URL = '{date:%Y}/{date:%m}/{date:%d}/{slug}/'
ARTICLE_SAVE_AS = '{date:%Y}/{date:%m}/{date:%d}/{slug}/index.html'

MONTH_ARCHIVE_SAVE_AS = '{date:%Y}/{date:%m}/index.html'
YEAR_ARCHIVE_SAVE_AS = '{date:%Y}/index.html'

SUMMARY_MAX_LENGTH = None
HIDE_SIDEBAR = True
DISPLAY_RECENT_POSTS_ON_SIDEBAR = True
DISPLAY_TAGS_ON_SIDEBAR = True
DISPLAY_TAGS_INLINE = True
TAG_CLOUD_MAX_ITEMS = 10

TYPOGRIFY = True


CC_LICENSE = 'CC-BY-NC-SA'

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
