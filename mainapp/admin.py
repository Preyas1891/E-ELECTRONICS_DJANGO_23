from django.contrib import admin
from .models import UserRegistration, ListingAppliances,OwnerDetails,Orders,ProperFeedback,paymentdetails

admin.site.register(UserRegistration)
admin.site.register(paymentdetails)
class ListingAppliancesAdmin(admin.ModelAdmin):
    list_display=['title','available']
admin.site.register(ListingAppliances)

admin.site.register([OwnerDetails,Orders])
admin.site.register(ProperFeedback)

admin.site.site_header = 'Administration Rental'                    # default: "Django Administration"
admin.site.index_title = 'Rental Admin APnel'                 # default: "Site administration"
admin.site.site_title = 'Adminsitration Panel'