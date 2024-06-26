
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("accounts.urls")),
    path('homework/', include("homework.urls")),
    path('notes/', include("notes.urls"))
]
