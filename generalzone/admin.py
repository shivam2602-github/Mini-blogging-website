from django.contrib import admin
from . models import Enquiry,CustomerInfo,LoginInfo

# Register your models here.
admin.site.register(Enquiry)
admin.site.register(LoginInfo)
admin.site.register(CustomerInfo)

