# -*- coding: utf-8 -*-

from django.db import models
from django.contrib import admin
from django.utils.translation import ugettext as _
from koalixcrm.crm.product.price import Price
from koalixcrm.crm.reporting.resource import Resource


class ResourcePrice(Price):
    resource = models.ForeignKey(Resource,
                                 verbose_name=_('Resource'),
                                 blank=False,
                                 null=False)


class ResourcePriceInlineAdminView(admin.TabularInline):
    model = ResourcePrice
    extra = 1
    classes = ['collapse']
    fieldsets = (
        ('Basic', {
            'fields': ('price',
                       'currency',
                       'unit',
                       'valid_from',
                       'valid_until',
                       'customer_group')
        }),
    )
    allow_add = True
