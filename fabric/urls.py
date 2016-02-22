from django.conf.urls import patterns, url

from views import *

urlpatterns = patterns('',
    url(r'^/fabric/(?P<fid>[1-9][0-9]*)/switch/(?P<sid>[1-9][0-9]*)/decommission$',
        FabricSwtichDecommissionView.as_view()),
    url(r'^/fabric/(?P<fid>[1-9][0-9]*)/link/(?P<lid>[1-9][0-9]*)$',
        FabricLinkDetailView.as_view()),
    url(r'^/fabric/(?P<fid>[1-9][0-9]*)/switch/(?P<sid>[1-9][0-9]*)$',
        FabricSwitchDetailView.as_view()),
    url(r'^/fabric/(?P<id>[1-9][0-9]*)/build$',
        FabricBuildView.as_view()),
    url(r'^/fabric/(?P<id>[1-9][0-9]*)/clone$',
        FabricCloneView.as_view()),
    url(r'^/fabric/(?P<id>[1-9][0-9]*)/defaults$',
        FabricDefaultsView.as_view()),
    url(r'^/fabric/(?P<id>[1-9][0-9]*)/link$',
        FabricLinkView.as_view()),
    url(r'^/fabric/(?P<id>[1-9][0-9]*)/profiles$',
        FabricProfilesView.as_view()),
    url(r'^/fabric/(?P<id>[1-9][0-9]*)/submit$',
        FabricSubmitView.as_view()),
    url(r'^/fabric/(?P<id>[1-9][0-9]*)/switch$',
        FabricSwitchView.as_view()),
    url(r'^/fabric/(?P<id>[1-9][0-9]*)$',
        FabricDetailView.as_view()),
    url(r'^/fabric$',
        FabricListView.as_view()),
    url(r'^/topology/(?P<tid>[1-9][0-9]*)/link/(?P<lid>[1-9][0-9]*)$',
        TopologyLinkDetailView.as_view()),
    url(r'^/topology/(?P<tid>[1-9][0-9]*)/switch/(?P<sid>[1-9][0-9]*)$',
        TopologySwitchDetailView.as_view()),
    url(r'^/topology/(?P<id>[1-9][0-9]*)/clear$',
        TopologyClearView.as_view()),
    url(r'^/topology/(?P<id>[1-9][0-9]*)/clone$',
        TopologyCloneView.as_view()),
    url(r'^/topology/(?P<id>[1-9][0-9]*)/defaults$',
        TopologyDefaultsView.as_view()),
    url(r'^/topology/(?P<id>[1-9][0-9]*)/link$',
        TopologyLinkView.as_view()),
    url(r'^/topology/(?P<id>[1-9][0-9]*)/submit$',
        TopologySubmitView.as_view()),
    url(r'^/topology/(?P<id>[1-9][0-9]*)/switch$',
        TopologySwitchView.as_view()),
    url(r'^/topology/(?P<id>[1-9][0-9]*)$',
        TopologyDetailView.as_view()),
    url(r'^/topology$',
        TopologyListView.as_view()),
)
