"""
This file was generated with the customdashboard management command and
contains the class for the main dashboard.

To activate your index dashboard add the following to your settings.py::
    GRAPPELLI_INDEX_DASHBOARD = 'nodeshot.dashboard.CustomIndexDashboard'
"""

from django.utils.translation import ugettext_lazy as _
from django.core.urlresolvers import reverse
from django.conf import settings

from grappelli.dashboard import modules, Dashboard
from grappelli.dashboard.utils import get_admin_site_name

USER_APPS = ['django.contrib.*']
if 'nodeshot.community.profiles' in settings.INSTALLED_APPS:
    USER_APPS.append('nodeshot.community.profiles.*')


class NodeshotDashboard(Dashboard):
    """
    Custom index dashboard for www.
    """
    
    def init_with_context(self, context):
        site_name = get_admin_site_name(context)
        
        self.children.append(modules.AppList(
            _('Nodeshot Core'),
            collapsible=True,
            column=1,
            models=('nodeshot.core.*',),
        ))
        
        self.children.append(modules.AppList(
            _('Nodeshot Networking'),
            collapsible=True,
            column=1,
            models=('nodeshot.networking.*',),
        ))
        
        self.children.append(modules.AppList(
            _('Nodeshot Community'),
            collapsible=True,
            column=1,
            models=('nodeshot.community.*',),
        ))
        
        self.children.append(modules.AppList(
            _('Administration'),
            collapsible=True,
            column=2,
            models=USER_APPS,
        ))
        
        # append a recent actions module
        self.children.append(modules.RecentActions(
            _('Recent Actions'),
            limit=5,
            collapsible=False,
            column=2,
        ))
        
        # append another link list module for "support".
        self.children.append(modules.LinkList(
            _('Media Management'),
            column=3,
            children=[
                {
                    'title': _('FileBrowser'),
                    'url': '/admin/filebrowser/browse/',
                    'external': False,
                },
            ]
        ))
        
        # append another link list module for "support".
        self.children.append(modules.LinkList(
            _('Support'),
            column=3,
            children=[
                {
                    'title': _('Django Documentation'),
                    'url': 'http://docs.djangoproject.com/',
                    'external': True,
                },
                {
                    'title': _('Grappelli Documentation'),
                    'url': 'http://packages.python.org/django-grappelli/',
                    'external': True,
                },
            ]
        ))
