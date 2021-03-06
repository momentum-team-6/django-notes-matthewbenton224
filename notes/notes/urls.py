"""notes URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf import settings
from django.urls import include, path
from core import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.list_notes, name='notes_list'),
    path('notes/<int:pk>/', views.note_detail, name='note_detail'),
    path('add-note/', views.add_note, name='add_note'),
    path('<int:pk>/delete_note/', views.delete_note, name='delete-note'),
    path('<int:pk>/edit_note/', views.edit_note, name='edit-note'),
    path('search/', views.search, name='search-bar'),
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),
        # For django versions before 2.0:
        # url(r'^__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns
