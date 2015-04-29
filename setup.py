#!/usr/bin/env python 2.7

from distutils.core import setup
setup( name='Scrumptious',
      description='Standup meeting preparation tool',
      url='https://github.com/ccolorado/scrumptious',
      packages=['jira.client', 'jinja2'],
      )
