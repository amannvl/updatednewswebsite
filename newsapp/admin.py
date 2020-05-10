from django.contrib import admin

from . models import  Contact, newslist, Newscatwise, Newscountrywise


from django.contrib import admin

admin.site.register(newslist)
admin.site.register(Contact)
admin.site.register(Newscatwise)
admin.site.register(Newscountrywise)
