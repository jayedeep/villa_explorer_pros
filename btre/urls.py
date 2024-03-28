from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from listings.views import import_listing_data

urlpatterns = [
    path('', include('pages.urls')),
    path('listings/', include('listings.urls')),
    path('accounts/', include('accounts.urls')),
    path('contacts/', include('contacts.urls')),
    path('admin/realtors/', include('realtors.urls')),
    path('admin/listings/', import_listing_data,name='import listing'),
    path('admin/', admin.site.urls),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
