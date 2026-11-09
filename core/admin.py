from django.contrib import admin
from .models import User, Subject, TutorProfile, Booking, Review

admin.site.register(User)
admin.site.register(Subject)
admin.site.register(TutorProfile)
admin.site.register(Booking)
admin.site.register(Review)
