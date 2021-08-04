"""barangay_information_system URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include


from barangay_information_system import settings
from barangay_information_app import HodViews, views

from barangay_information_app import StaffViews

urlpatterns = [
    path('demo', views.showDemoPage),
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('', views.ShowLoginPage, name="show_login"),
    path('get_user_details', views.GetUserDetails),
    path('logout_user', views.logout_user, name="logout"),
    path('doLogin', views.doLogin, name="do_login"),
    path('admin_home', HodViews.admin_home, name="admin_home"),
    path('add_official', HodViews.add_official, name="add_official"),
    path('add_official_save', HodViews.add_official_save, name="add_official_save"),
    path('add_purok', HodViews.add_purok, name="add_purok"),
    path('add_purok_save', HodViews.add_purok_save, name="add_purok_save"),
    path('add_staff', HodViews.add_staff, name="add_staff"),
    path('add_staff_save', HodViews.add_staff_save, name="add_staff_save"),
    path('add_household', HodViews.add_household, name="add_household"),
    path('add_household_save', HodViews.add_household_save, name="add_household_save"),
    path('add_report', HodViews.add_report, name="add_report"),
    path('add_report_save', HodViews.add_report_save, name="add_report_save"),
    path('staff_take_attendance_save', HodViews.staff_take_attendance_save, name="staff_take_attendance_save"),
    path('view_attendance', HodViews.view_attendance, name="view_attendance"),
    path('manage_staff', HodViews.manage_staff, name="manage_staff"),
    path('manage_household', HodViews.manage_household, name="manage_household"),
    path('manage_purok', HodViews.manage_purok, name="manage_purok"),
    path('manage_official', HodViews.manage_official, name="manage_official"),
    path('manage_report', HodViews.manage_report, name="manage_report"),
    path('view_attendance', HodViews.view_attendance, name="view_attendance"),
    path('edit_staff/<str:staff_id>', HodViews.edit_staff, name="edit_staff"),
    path('edit_staff_save', HodViews.edit_staff_save, name="edit_staff_save"),
    path('edit_household/<str:household_id>', HodViews.edit_household, name="edit_household"),
    path('edit_household_save', HodViews.edit_household_save, name="edit_household_save"),
    path('edit_purok/<str:purok_id>', HodViews.edit_purok, name="edit_purok"),
    path('edit_purok_save', HodViews.edit_purok_save, name="edit_purok_save"),
    path('edit_official/<str:official_id>', HodViews.edit_official, name="edit_official"),
    path('edit_official_save', HodViews.edit_official_save, name="edit_official_save"),
    path('edit_report/<str:report_id>', HodViews.edit_report, name="edit_report"),
    path('edit_report_save', HodViews.edit_report_save, name="edit_report_save"),
    path('admin_profile', HodViews.admin_profile, name="admin_profile"),
    path('admin_profile_save', HodViews.admin_profile_save, name="admin_profile_save"),
#     Staff URL Path
    path('staff_home', StaffViews.staff_home, name="staff_home"),
    path('staff_take_attendance', StaffViews.staff_take_attendance, name="staff_take_attendance"),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)+static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
