# -*- coding: UTF-8 -*-
# __author__ : RobbieHan
# __data__  : 2017/12/8

from django.conf.urls import url

from adm import views_company

urlpatterns = [

    url(r'^corp$', views_company.CompanyCorpView.as_view(), name='corp'),
    url(r'^corp_list', views_company.CompanyCorpListView.as_view(), name="corp-list"),
    url(r'^corp_create', views_company.CompanyCorpCreateView.as_view(), name="corp-create"),
    # url(r'^detail', views_equipment.EquipmentDetailView.as_view(), name="equipment-detail"),
    # url(r'^delete', views_equipment.EquipmentDeleteView.as_view(), name='delete'),
    # url(r'^serviceinfoupdate', views_equipment.ServiceInfoUpdateView.as_view(), name='service-info-update'),
]
