#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Naomi See'
SITENAME = 'Naomi did a thing'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'America/Chicago'

THEME = '/home/seenaomi/opt/pelican-themes/BT3-Flat'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pyladies Remote', 'http://remote.pyladies.com/index.html'),
         ('Omaha Python UG', 'https://www.meetup.com/Omahas-Python-Users-Group/'),
         ('Tech Omaha', 'http://techomaha.com/'),
         ('Full Stack Python', 'https://www.fullstackpython.com/'),)

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

# DEFAULT_PAGINATION = True
# PAGINATED_DIRECT_TEMPLATES = ('blog-index',)
# DIRECT_TEMPLATES = ('categories', 'index', 'blog-index', 'blog')

POST_LIMIT = 3

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

#===theme settings===========================

FAVICON = ''
ICON = ''
SHORTCUT_ICON = ''
HEADER_IMAGE = ''
BACKGROUND_IMAGE = 'https://streets-united.com/wp-content/uploads/2012/08/floating-umbrellas-installation-agueda-portugal-7.jpg'
# COPYRIGHT = '2015 &copy; All Rights Reserved.'
# Google fonts can be downloaded with
# https://neverpanic.de/downloads/code/2014-03-19-downloading-google-web-fonts-for-local-hosting-fetch.sh'
# Maybe you need to add missing mime types to your webserver configuration
# USER_FONT = '/theme/fonts/font.css'
# USER_BOOTSTRAP = '//maxcdn.bootstrapcdn.com/bootstrap/3.3.4'
# USER_FONTAWESOME = '//maxcdn.bootstrapcdn.com/font-awesome/4.3.0'
# USER_JQUERY = '//code.jquery.com/jquery-1.11.2.min.js'

# About ME
PERSONAL_PHOTO = ""
PERSONAL_INFO = """"""

# work
WORK_DESCRIPTION = ''
# items to descripe a work, "type", "cover-image link", "title", "descption", "link"
# WORK_LIST = (('link', 'https://dl.dropboxusercontent.com/u/299446/BT3-Flat.png', 'BT3-Flat', 'A BT3 flat theme for pelican', 'https://github.com/KenMercusLai/plumage'),)