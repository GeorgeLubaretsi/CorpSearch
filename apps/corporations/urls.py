from django.conf.urls import *
from .views import CorporationCsvSearchView, CorporationPagedTemplateSearchView, CorporationDetailView

urlpatterns = patterns('',
    # This will show every corporation on one page. Since there are now 150,000+
    # corporations, this is not recommended.
    #url(r'^$', CorporationListView.as_view(template_name="corporations/corporation_list.html"), name='corporation-list'),

    url(r'^(?P<id_code>\d+)/$', CorporationDetailView.as_view(template_name="corporations/detail.html"), name='corporation-detail'),
    url(r'^search/$', CorporationPagedTemplateSearchView.as_view(template_name="corporations/corporation_list.html"), name='corporation-search'),
    url(r'^search/csv/$', CorporationCsvSearchView.as_view(), name='corporation-search-csv'),
)
